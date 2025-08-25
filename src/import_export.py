"""Import and export utilities."""
from __future__ import annotations

import io
from pathlib import Path
from typing import Iterable

import pandas as pd
import streamlit as st

from .db import get_session
from .repository import LeadRepository


def import_from_excel(path: str | Path) -> int:
    """Import leads from an Excel file into the database.

    Returns the number of imported rows.
    """

    df = pd.read_excel(path, sheet_name="Leads")
    df.columns = [c.strip().lower() for c in df.columns]
    session = get_session()
    repo = LeadRepository(session)
    count = 0
    for _, row in df.iterrows():
        data = {k: (v.to_pydatetime().date() if hasattr(v, "to_pydatetime") else v) for k, v in row.items() if pd.notna(v)}
        repo.add(data)
        count += 1
    return count


def export_dataframe(df: pd.DataFrame, fmt: str = "csv") -> bytes:
    """Return dataframe serialized to the given format."""
    buf = io.BytesIO()
    if fmt == "csv":
        df.to_csv(buf, index=False)
    else:
        df.to_excel(buf, index=False)
    return buf.getvalue()
