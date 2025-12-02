"""CRM Opportunity API placeholders used in the interview challenge."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.opportunity import OpportunityCreate, OpportunityRead

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
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail=(
            "Challenge 2: Insert a row into `crm_opportunities` and return the stored "
            "record. Ensure the payload references an existing customer. "
            "See README for the step-by-step outline."
        ),
    )


