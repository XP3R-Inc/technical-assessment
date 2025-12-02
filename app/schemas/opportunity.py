"""Pydantic schemas for CRM opportunities."""

from __future__ import annotations

from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field


class OpportunityBase(BaseModel):
    """Fields shared by create/read schemas."""

    cid: int = Field(description="Foreign key referencing customer.cid")
    opportunity_sales_group: str | None = Field(default=None, max_length=32)
    opportunity_status: str | None = Field(default=None, max_length=32)
    monthly_estimated_revenue: Decimal | None = Field(default=None)
    estimated_delivery_date: date | None = Field(default=None)
    non_recurring: str | None = Field(default=None, max_length=32)
    days_since_last_updated: int | None = Field(default=None, ge=0)


class OpportunityCreate(OpportunityBase):
    """Incoming payload when creating CRM opportunities."""

    ...


class OpportunityRead(OpportunityBase):
    """Response payload returned after creation."""

    oid: str

    model_config = {"from_attributes": True}


