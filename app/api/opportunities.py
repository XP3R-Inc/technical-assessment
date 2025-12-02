"""CRM Opportunity API placeholders used in the interview challenge."""

from __future__ import annotations

from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import get_db
from app.schemas.opportunity import OpportunityCreate, OpportunityRead
from app.models.customer import Customer
from app.models.opportunity import Opportunities

router = APIRouter()


@router.post(
    "",
    response_model=OpportunityRead,
    status_code=status.HTTP_201_CREATED,
)
def create_opportunities(
    payload: OpportunityCreate, db: Session = Depends(get_db)
) -> OpportunityRead: 
    customer =db.query(Customer).fiilter(Customer.cid == payload.cid).first()
    if customer is None: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Customer with cid={payload.cid} does not exist."
        )
    oid = uuid4.hex

    opp = Opportunities(
        oid:oid,
        cid:payload.cid
        opportunity_status=payload.opportunity_status,
        estimated_monthly_revenue=payload.estimated_monthly_revenue,
        estimated_delivery_date=payload.estimated_delivery_date,
    )
    try:   
        db.add(opp)   
        db.commit()
        db.refresh(opp)
    except SQLAlchemyError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= "Database error while creating opportunity.",
        )from exc
    return opp


