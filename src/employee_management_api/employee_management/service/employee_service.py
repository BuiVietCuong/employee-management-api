from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session

from ..config.util import ORG_FIELD_CONFIG
from ..repository import employee_repository

# Example org config for allowed fields per org ID (lowercase keys)



def search_employees(
        db: Session,
        status: Optional[List[str]],
        location: Optional[str],
        company: Optional[str],
        department: Optional[str],
        position: Optional[str],
        organization_id: str,
) -> List[Dict[str, Any]]:
    employees = employee_repository.query_employees(
        db=db,
        status=status,
        location=location,
        company=company,
        department=department,
        position=position,
    )

    allowed_fields = ORG_FIELD_CONFIG.get(organization_id.lower(), [])
    result = []
    for emp in employees:
        filtered = {field: getattr(emp, field) for field in allowed_fields if hasattr(emp, field)}
        result.append(filtered)
    return result
