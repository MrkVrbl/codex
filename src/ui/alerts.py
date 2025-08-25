"""Alert utilities."""
from __future__ import annotations

from datetime import date, timedelta

import pandas as pd
import streamlit as st


def alerts_box(df: pd.DataFrame) -> None:
    if df.empty or "datum_dalsieho_kroku" not in df.columns:
        return
    today = pd.to_datetime(date.today())
    upcoming = df.dropna(subset=["datum_dalsieho_kroku"])
    upcoming["datum_dalsieho_kroku"] = pd.to_datetime(upcoming["datum_dalsieho_kroku"])
    overdue = upcoming[upcoming["datum_dalsieho_kroku"] < today]
    today_df = upcoming[upcoming["datum_dalsieho_kroku"] == today]
    next_week = upcoming[(upcoming["datum_dalsieho_kroku"] > today) & (upcoming["datum_dalsieho_kroku"] <= today + timedelta(days=7))]
    st.info(f"Po termíne: {len(overdue)} | Dnes: {len(today_df)} | 7 dní: {len(next_week)}")
