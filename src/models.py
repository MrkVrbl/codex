"""Database models."""
from __future__ import annotations

from sqlalchemy import Column, Integer, String, Date, Float

from .db import Base


class Lead(Base):
    """CRM lead model."""

    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    meno_zakaznika = Column(String, nullable=False)
    telefon = Column(String)
    email = Column(String)
    mesto = Column(String)
    typ_dopytu = Column(String)
    datum_povodneho_kontaktu = Column(Date)
    stav_projektu = Column(String)
    konkurencia = Column(String)
    cena_konkurencie = Column(Float)
    nasa_ponuka_orientacna = Column(Float)
    reakcia_zakaznika = Column(String)
    dalsi_krok = Column(String)
    datum_dalsieho_kroku = Column(Date)
    priorita = Column(String)
    stav_leadu = Column(String)
    orientacna_cena = Column(Float)
    datum_realizacie = Column(Date)
    poznamky = Column(String)
