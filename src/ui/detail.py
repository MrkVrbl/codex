"""Lead detail view."""
from __future__ import annotations

import pandas as pd
import streamlit as st

from ..db import get_session
from ..repository import LeadRepository


def render_detail(lead_id: int) -> None:
    session = get_session()
    repo = LeadRepository(session)
    lead = repo.get(lead_id)
    if lead is None:
        st.error("Lead nenájdený")
        return
    data = {c.name: getattr(lead, c.name) for c in lead.__table__.columns}
    df = pd.DataFrame([data])
    edited = st.data_editor(df, num_rows=1)
    if st.button("Uložiť"):
        repo.update(lead_id, edited.iloc[0].to_dict())
        st.success("Uložené")
