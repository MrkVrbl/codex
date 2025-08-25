"""Repository layer for database operations."""
from __future__ import annotations

from typing import Iterable, List

from sqlalchemy.orm import Session

from . import models


class LeadRepository:
    """CRUD operations for :class:`~models.Lead`."""

    def __init__(self, session: Session):
        self.session = session

    def all(self) -> List[models.Lead]:
        return self.session.query(models.Lead).all()

    def get(self, lead_id: int) -> models.Lead | None:
        return self.session.get(models.Lead, lead_id)

    def add(self, data: dict) -> models.Lead:
        lead = models.Lead(**data)
        self.session.add(lead)
        self.session.commit()
        self.session.refresh(lead)
        return lead

    def update(self, lead_id: int, data: dict) -> models.Lead:
        lead = self.get(lead_id)
        if lead is None:
            raise ValueError("Lead not found")
        for key, value in data.items():
            setattr(lead, key, value)
        self.session.commit()
        return lead

    def delete(self, lead_id: int) -> None:
        lead = self.get(lead_id)
        if lead:
            self.session.delete(lead)
            self.session.commit()
