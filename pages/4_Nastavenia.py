import streamlit as st

from src.ui.layout import init_page
from src.auth import login
from src.db import init_db

init_page()
init_db()
authenticator, role = login()
authenticator.logout("Odhlásiť", "sidebar")

st.header("Nastavenia")
st.write("Zoznam povolených e-mailov:")
st.write(st.secrets.get("auth", {}).get("allowed_emails", []))
