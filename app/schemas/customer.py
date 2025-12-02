"""Pydantic schemas for Customer records."""

from __future__ import annotations

from pydantic import BaseModel, Field


class CustomerRead(BaseModel):
    """Response schema for Challenge 1."""

    cid: int = Field(description="Customer identifier")
    area: str | None = Field(default=None)
    customer_type: str | None = Field(default=None)
    has_dedicated_account_manager: bool
    has_dedicated_technical_consultant: bool
    has_support_contract: bool
    has_discounted_pricing: bool

    model_config = {"from_attributes": True}


