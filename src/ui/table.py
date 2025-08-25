"""Leads table view."""
from __future__ import annotations

import pandas as pd
import streamlit as st

from ..db import get_session
from ..repository import LeadRepository
from .forms import new_lead_form
from .detail import render_detail
from .alerts import alerts_box


STATUS_COLORS = {
    "Open": "#fff3cd",
    "Cold": "#dceef9",
    "Converted": "#d4edda",
    "Lost": "#f8d7da",
}
PRIORITY_COLORS = {
    "Vysoká": "#f8d7da",
    "Stredná": "#ffe5b4",
    "Nízka": "#dceef9",
}


def _style_row(row: pd.Series) -> list[str]:
    color = STATUS_COLORS.get(row.get("stav_leadu"), "")
    return [f"background-color: {color}"] * len(row)


def leads_table() -> None:
    session = get_session()
    repo = LeadRepository(session)
    leads = repo.all()
    if not leads:
        st.info("Žiadne leady. Importujte alebo pridajte nový.")
    df = pd.DataFrame([l.__dict__ for l in leads]).drop(columns=["_sa_instance_state"], errors="ignore")

    alerts_box(df)

    with st.expander("Filtre", expanded=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            status_filter = st.multiselect("Stav leadu", sorted(df["stav_leadu"].dropna().unique()))
        with col2:
            priority_filter = st.multiselect("Priorita", sorted(df["priorita"].dropna().unique()))
        with col3:
            typ_filter = st.multiselect("Typ dopytu", sorted(df["typ_dopytu"].dropna().unique()))
        search = st.text_input("Fulltext")

    if status_filter:
        df = df[df["stav_leadu"].isin(status_filter)]
    if priority_filter:
        df = df[df["priorita"].isin(priority_filter)]
    if typ_filter:
        df = df[df["typ_dopytu"].isin(typ_filter)]
    if search:
        df = df[df.apply(lambda r: r.astype(str).str.contains(search, case=False, na=False).any(), axis=1)]

    editable_cols = [
        "stav_leadu",
        "priorita",
        "stav_projektu",
        "dalsi_krok",
        "datum_dalsieho_kroku",
        "poznamky",
        "nasa_ponuka_orientacna",
    ]

    edited = st.data_editor(
        df.style.apply(_style_row, axis=1),
        use_container_width=True,
        disabled=[c for c in df.columns if c not in editable_cols],
    )

    if not edited.equals(df):
        for _, row in edited.iterrows():
            orig = df[df["id"] == row["id"]].iloc[0]
            changed = {
                col: row[col]
                for col in editable_cols
                if str(row[col]) != str(orig[col])
            }
            if changed:
                repo.update(int(row["id"]), changed)
        st.experimental_rerun()

    st.divider()
    st.subheader("Detail")
    if not df.empty:
        selected_id = st.selectbox("Vyber lead", df["id"].tolist())
        if selected_id:
            render_detail(int(selected_id))

    st.divider()
    if st.button("Nový lead"):
        new_lead_form(repo)
