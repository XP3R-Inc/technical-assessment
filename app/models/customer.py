"""SQLAlchemy model for Customer records."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base

if TYPE_CHECKING:
    from app.models.opportunity import CrmOpportunity


class Customer(Base):
    """Represents a record in the `customer` table."""

    __tablename__ = "customer"

    cid: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    area: Mapped[str | None] = mapped_column(String(32), nullable=True)
    customer_type: Mapped[str | None] = mapped_column(String(32), nullable=True)
    has_dedicated_account_manager: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    has_dedicated_technical_consultant: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    has_support_contract: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    has_discounted_pricing: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )

    opportunities: Mapped[list["CrmOpportunity"]] = relationship(
        back_populates="customer",
    )


