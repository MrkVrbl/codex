"""Main entry for REMARK CRM."""
from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

# Ensure project root is on the Python path when running as a script
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.db import init_db
from src.ui.layout import init_page
from src.auth import login


def main() -> None:
    init_page()
    init_db()
    authenticator, role = login()
    authenticator.logout("Odhlásiť", "sidebar")
    st.write("Vitajte v REMARK CRM. Použite menu vľavo na navigáciu.")


if __name__ == "__main__":
    main()
