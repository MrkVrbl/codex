"""Main entry for REMARK CRM."""
from __future__ import annotations

import streamlit as st

from .db import init_db
from .ui.layout import init_page
from .auth import login


def main() -> None:
    init_page()
    init_db()
    authenticator, role = login()
    authenticator.logout("Odhlásiť", "sidebar")
    st.write("Vitajte v REMARK CRM. Použite menu vľavo na navigáciu.")


if __name__ == "__main__":
    main()
