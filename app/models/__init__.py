"""SQLAlchemy models package exports."""

from app.models.customer import Customer
from app.models.opportunity import CrmOpportunity

__all__ = ["Customer", "CrmOpportunity"]

