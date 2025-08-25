# REMARK CRM

Streamlit aplikácia pre správu leadov pre firmu REMARK Interier.

## Spustenie

```bash
pip install -r requirements.txt
streamlit run src/app.py
```

## Konfigurácia `secrets.toml`
Všetky citlivé údaje sú mimo repozitára a ukladajú sa do `secrets.toml` v Streamlit Cloud.
Príklad konfigurácie:

```toml
[db]
connection = "sqlite:///data/remark_crm.db"  # alebo Postgres connection string

[auth]
allowed_emails = ["user@example.com"]

[[auth.users]]
email = "user@example.com"
name = "User"
password = "hashed_password"

[auth.roles]
"user@example.com" = "admin"

[auth.cookie]
name = "remark_crm"
key = "some-secret-key"
expiry_days = 1
```

- `allowed_emails` určuje, kto sa môže prihlásiť.
- `auth.roles` definuje rolu používateľa (`admin` alebo `user`).
- Export dát je dostupný iba pre rolu `admin`.

## Stránky
- **Leads** – prehľad a správa leadov.
- **Summary** – štatistiky a grafy.
- **Import/Export** – import z Excelu a export do CSV/XLSX.
- **Nastavenia** – prehľad povolených e-mailov.

Dátová schéma vychádza zo súboru `CRM_leads_REMARK_FIXED.xlsx` (nie je súčasťou repozitára; umiestnite ho do `data/seed/` podľa potreby).
