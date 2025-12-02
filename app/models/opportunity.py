"""SQLAlchemy model for CRM opportunities."""

from __future__ import annotations

from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base

if TYPE_CHECKING:
    from app.models.customer import Customer


class CrmOpportunity(Base):
    """Represents a record in the `crm_opportunities` table."""

    __tablename__ = "crm_opportunities"

    oid: Mapped[str] = mapped_column(String(32), primary_key=True)
    cid: Mapped[int] = mapped_column(
        ForeignKey("customer.cid", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    opportunity_sales_group: Mapped[str | None] = mapped_column(String(32))
    opportunity_status: Mapped[str | None] = mapped_column(String(32))
    monthly_estimated_revenue: Mapped[Decimal | None] = mapped_column(
        Numeric(18, 2), nullable=True
    )
    estimated_delivery_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    non_recurring: Mapped[str | None] = mapped_column(String(32))
    days_since_last_updated: Mapped[int | None] = mapped_column(Integer)

    customer: Mapped["Customer"] = relationship(back_populates="opportunities")


