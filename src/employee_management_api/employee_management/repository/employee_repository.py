from typing import List, Optional
from sqlalchemy.orm import Session
from ..model.employee import Employee

def query_employees(
    db: Session,
    status: Optional[List[str]],
    location: Optional[str],
    company: Optional[str],
    department: Optional[str],
    position: Optional[str],
) -> List[Employee]:
    query = db.query(Employee)
    if status:
        query = query.filter(Employee.status.in_(status))
    if location:
        query = query.filter(Employee.location == location)
    if company:
        query = query.filter(Employee.company == company)
    if department:
        query = query.filter(Employee.department == department)
    if position:
        query = query.filter(Employee.position == position)
    return query.all()
