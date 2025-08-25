import streamlit as st
import pandas as pd

from src.ui.layout import init_page
from src.auth import login
from src.db import init_db, get_session
from src.import_export import import_from_excel, export_dataframe
from src.repository import LeadRepository

init_page()
init_db()
authenticator, role = login()
authenticator.logout("Odhlásiť", "sidebar")

st.header("Import / Export")

uploaded = st.file_uploader("Excel súbor", type=["xlsx"])
if uploaded and st.button("Importovať"):
    count = import_from_excel(uploaded)
    st.success(f"Importovaných {count} záznamov")

session = get_session()
repo = LeadRepository(session)
leads = repo.all()
df = pd.DataFrame([l.__dict__ for l in leads]).drop(columns=["_sa_instance_state"], errors="ignore")

if role == "admin" and not df.empty:
    fmt = st.selectbox("Formát", ["csv", "xlsx"])
    data = export_dataframe(df, fmt)
    mime = "text/csv" if fmt == "csv" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    st.download_button("Export", data=data, file_name=f"leads.{fmt}", mime=mime)
else:
    st.info("Export je dostupný len administrátorom")
