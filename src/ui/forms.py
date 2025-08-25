"""Forms used in the application."""
from __future__ import annotations

from datetime import date

import streamlit as st

from ..repository import LeadRepository


def new_lead_form(repo: LeadRepository) -> None:
    """Form for creating a new lead."""
    with st.form("new-lead"):
        meno = st.text_input("Meno zákazníka")
        telefon = st.text_input("Telefón")
        email = st.text_input("Email")
        mesto = st.text_input("Mesto")
        typ = st.text_input("Typ dopytu")
        datum_kontaktu = st.date_input("Dátum pôvodného kontaktu", value=date.today())
        stav_projektu = st.text_input("Stav projektu")
        konkurencia = st.text_input("Konkurencia")
        cena_konkurencie = st.number_input("Cena konkurencie", min_value=0.0, step=100.0)
        nasa_ponuka = st.number_input("Naša ponuka orientačná", min_value=0.0, step=100.0)
        reakcia = st.text_input("Reakcia zákazníka")
        dalsi_krok = st.text_input("Ďalší krok")
        datum_kroku = st.date_input("Dátum ďalšieho kroku")
        priorita = st.selectbox("Priorita", ["Vysoká", "Stredná", "Nízka"])
        stav_leadu = st.selectbox("Stav leadu", ["Open", "Cold", "Converted", "Lost"])
        orientacna_cena = st.number_input("Orientačná cena", min_value=0.0, step=100.0)
        datum_realizacie = st.date_input("Dátum realizácie", value=None)
        poznamky = st.text_area("Poznámky")
        submitted = st.form_submit_button("Uložiť")
    if submitted:
        repo.add({
            "meno_zakaznika": meno,
            "telefon": telefon,
            "email": email,
            "mesto": mesto,
            "typ_dopytu": typ,
            "datum_povodneho_kontaktu": datum_kontaktu,
            "stav_projektu": stav_projektu,
            "konkurencia": konkurencia,
            "cena_konkurencie": cena_konkurencie,
            "nasa_ponuka_orientacna": nasa_ponuka,
            "reakcia_zakaznika": reakcia,
            "dalsi_krok": dalsi_krok,
            "datum_dalsieho_kroku": datum_kroku,
            "priorita": priorita,
            "stav_leadu": stav_leadu,
            "orientacna_cena": orientacna_cena,
            "datum_realizacie": datum_realizacie,
            "poznamky": poznamky,
        })
        st.success("Lead pridaný")
        st.experimental_rerun()
