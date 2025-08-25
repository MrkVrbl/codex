"""Authentication helpers."""
from __future__ import annotations

import streamlit as st
import streamlit_authenticator as stauth


def login() -> tuple[stauth.Authenticate, str]:
    """Authenticate user and return authenticator and role."""
    auth_conf = st.secrets.get("auth", {})
    credentials = {"usernames": {}}
    for user in auth_conf.get("users", []):
        credentials["usernames"][user["email"]] = {
            "email": user["email"],
            "name": user.get("name", user["email"]),
            "password": user["password"],
        }

    authenticator = stauth.Authenticate(
        credentials,
        auth_conf.get("cookie", {}).get("name", "crm"),
        auth_conf.get("cookie", {}).get("key", "key"),
        auth_conf.get("cookie", {}).get("expiry_days", 1),
    )

    authenticator.login(location="main", key="Login")

    if not st.session_state.get("authentication_status"):
        st.warning("Please enter your credentials")
        st.stop()

    username = st.session_state.get("username", "")
    allowed = username in auth_conf.get("allowed_emails", [])
    if not allowed:
        st.error("Access denied")
        st.stop()

    role = auth_conf.get("roles", {}).get(username, "user")
    st.session_state["role"] = role
    return authenticator, role
