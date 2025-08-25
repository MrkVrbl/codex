"""Database setup and utilities."""
from __future__ import annotations

import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
_engine = None
_SessionLocal = None


def get_engine():
    """Return a SQLAlchemy engine using the connection in ``st.secrets``."""
    global _engine, _SessionLocal
    if _engine is None:
        db_url = st.secrets.get("db", {}).get("connection", "sqlite:///data/remark_crm.db")
        if db_url.startswith("sqlite"):
            _engine = create_engine(db_url, connect_args={"check_same_thread": False})
        else:
            _engine = create_engine(db_url)
        _SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
    return _engine


def get_session():
    """Return a new SQLAlchemy session."""
    global _SessionLocal
    if _SessionLocal is None:
        get_engine()
    return _SessionLocal()


def init_db():
    """Create database tables."""
    engine = get_engine()
    Base.metadata.create_all(bind=engine)
