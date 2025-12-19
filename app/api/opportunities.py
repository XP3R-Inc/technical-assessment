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
    """
    Challenge 2 – Create a CRM opportunity tied to a customer.

    - Accepts an OpportunityCreate payload validated by Pydantic.
    - Ensures the referenced customer (cid) exists before inserting.
    - Generates a unique primary key (oid) in the application layer.
    - Commits the transaction and returns the persisted record.
    """
    try:
        # 1 Validate that the referenced customer exists
        # Using db.get() performs a primary-key lookup and is efficient
        customer = db.get(Customer, payload.cid)
        if customer is None:
            # Return a 404 if the foreign key reference is invalid
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer with cid={payload.cid} not found.",
            )

        # 2 Create a new CRM opportunity ORM object
        # uuid4().hex ensures a globally unique 32-character identifier
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

        # 3 Persist the object to the database
        db.add(opp)
        db.commit()       # Commit the transaction
        db.refresh(opp)  # Refresh to ensure all DB-generated values are loaded

        # Return the ORM object
        # FastAPI serializes it into OpportunityRead using from_attributes=True
        return opp

    except HTTPException:
        # Re-raise intentional HTTP errors e.g., 404
        # This prevents them from being incorrectly wrapped as 500s
        raise

    except SQLAlchemyError as e:
        # Roll back the transaction to prevent partial or failed writes
        db.rollback()

        # Return a generic server error without exposing internal details
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error while creating opportunity.",
        ) from e
