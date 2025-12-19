"""Customer API placeholders used in the interview challenge."""

from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.customer import CustomerRead

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.models.customer import Customer
router = APIRouter()


@router.get("", response_model=List[CustomerRead])
def list_customers(db: Session = Depends(get_db)) -> List[CustomerRead]:
    """
    Challenge 1 – Fetch every customer from MySQL.

    - Uses FastAPI dependency injection to receive a database session.
    - Queries all rows from the `customer` table using the Customer ORM model.
    - Returns ORM objects that FastAPI serializes into CustomerRead schemas.
    """
    try:
        # Execute a SELECT query against the customer table
        # `select(Customer)` builds a SQL SELECT using the ORM model
        customers = db.execute(select(Customer)).scalars().all()

        # Return the list of ORM objects
        # FastAPI + Pydantic (from_attributes=True) handle serialization
        return customers

    except SQLAlchemyError as e:
        # Roll back the session to ensure no partial or failed transaction
        # leaves the session in an invalid state
        db.rollback()

        # Return a generic 500 error so internal DB details are not exposed
        # to API consumers
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error while fetching customers.",
        ) from e
