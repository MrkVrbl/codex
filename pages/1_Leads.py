import streamlit as st

from src.ui.layout import init_page
from src.auth import login
from src.db import init_db
from src.ui.table import leads_table

init_page()
init_db()
authenticator, role = login()
authenticator.logout("Odhlásiť", "sidebar")
leads_table()
