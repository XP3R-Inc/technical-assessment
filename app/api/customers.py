"""Customer API placeholders used in the interview challenge."""

from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.customer import CustomerRead

router = APIRouter()


@router.get("", response_model=List[CustomerRead])
def list_customers(db: Session = Depends(get_db)) -> List[CustomerRead]:
    """Challenge 1 – fetch every customer from MySQL."""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail=(
            "Challenge 1: Query the `customer` table and return every row using the "
            "`CustomerRead` schema. See README for full instructions."
        ),
    )


