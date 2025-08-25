"""Summary and statistics page."""
from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from ..db import get_session
from ..repository import LeadRepository


def summary_view() -> None:
    session = get_session()
    repo = LeadRepository(session)
    leads = repo.all()
    df = pd.DataFrame([l.__dict__ for l in leads]).drop(columns=["_sa_instance_state"], errors="ignore")
    if df.empty:
        st.info("Žiadne dáta")
        return

    st.subheader("Počty leadov podľa stavu")
    fig = px.bar(df.groupby("stav_leadu").size().reset_index(name="count"), x="stav_leadu", y="count")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Počty podľa priority")
    fig = px.pie(df, names="priorita")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Trend nových leadov")
    df["datum_povodneho_kontaktu"] = pd.to_datetime(df["datum_povodneho_kontaktu"])
    trend = df.groupby(pd.Grouper(key="datum_povodneho_kontaktu", freq="M")).size().reset_index(name="count")
    fig = px.line(trend, x="datum_povodneho_kontaktu", y="count")
    st.plotly_chart(fig, use_container_width=True)
