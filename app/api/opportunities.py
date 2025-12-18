"""CRM Opportunity API placeholders used in the interview challenge."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.opportunity import OpportunityCreate, OpportunityRead

from uuid import uuid4

from sqlalchemy.exc import SQLAlchemyError

from app.models.customer import Customer
from app.models.opportunity import CrmOpportunity

router = APIRouter()


@router.post(
    "",
    response_model=OpportunityRead,
    status_code=status.HTTP_201_CREATED,
)
def create_opportunity(
    payload: OpportunityCreate, db: Session = Depends(get_db)
) -> OpportunityRead:
    """Challenge 2 – create a CRM opportunity tied to a customer."""
    try:
        # 1) Validate customer exists
        customer = db.get(Customer, payload.cid)
        if customer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer with cid={payload.cid} not found.",
            )

        # 2) Create the opportunity (generate oid)
        opp = CrmOpportunity(
            oid=uuid4().hex,
            cid=payload.cid,
            opportunity_sales_group=payload.opportunity_sales_group,
            opportunity_status=payload.opportunity_status,
            monthly_estimated_revenue=payload.monthly_estimated_revenue,
            estimated_delivery_date=payload.estimated_delivery_date,
            non_recurring=payload.non_recurring,
            days_since_last_updated=payload.days_since_last_updated,
        )

        db.add(opp)
        db.commit()
        db.refresh(opp)
        return opp

    except HTTPException:
        # re-raise validation errors (like 404) without masking them
        raise
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error while creating opportunity.",
        ) from e

