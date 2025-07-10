import logging

from fastapi import APIRouter, Depends, Query, Header
from sqlalchemy.orm import Session
from ...db.my_sql import get_db
from typing import List, Optional
from ...service import employee_service

logging.basicConfig(level=logging.INFO)
router = APIRouter()

@router.get("/health", tags=["Health"])
def health_check():
    logging.info("hahhaa")
    return {"status": "OK"}


@router.get("/employees/search")
def search_employees_api(
        status: Optional[List[str]] = Query(None),
        location: Optional[str] = None,
        company: Optional[str] = None,
        department: Optional[str] = None,
        position: Optional[str] = None,
        organization_id: str = Header(...),
        db: Session = Depends(get_db)
):
    logging.info("search_employees_api")
    employees = employee_service.search_employees(
        db=db,
        status=status,
        location=location,
        company=company,
        department=department,
        position=position,
        organization_id=organization_id,
    )
    return employees