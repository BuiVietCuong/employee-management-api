from ..db.my_sql import Base
from sqlalchemy import Column, Integer, String

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    department = Column(String(50))
    position = Column(String(50))
    location = Column(String(50))
    status = Column(String(50))