"""Customer API placeholders used in the interview challenge."""

from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.customer import CustomerRead
from app.models.customer import Customer
router = APIRouter()


@router.get("", response_model=List[CustomerRead])
def list_customers(db: Session = Depends(get_db)) -> List[CustomerRead]:
    """Challenge 1: fetch every customer from MySQL."""
    try:
        customers = db.query(Customer).all()
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error while fetching customers.",
        ) from exc

    return customers


