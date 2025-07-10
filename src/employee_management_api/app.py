from fastapi import FastAPI, Request
from .employee_management.routers.employee.api import router as employee_api_router
from .employee_management.db import Base, engine, SessionLocal
from .employee_management.model.employee import Employee
from .middleware import CacheMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded


app = FastAPI()

# Set up the limiter (e.g., 5 requests per minute)
limiter = Limiter(key_func=get_remote_address)


# Register middleware and error handler
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
# Include all API routes under root or a prefix
app.include_router(employee_api_router)
app.add_middleware(CacheMiddleware, ttl=60)
limiter = Limiter(key_func=get_remote_address, default_limits=["100/hour"])  # 100 requests/hour per IP


@app.on_event("startup")
def startup():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)

    # Seed initial data (optional)
    db = SessionLocal()
    if db.query(Employee).count() == 0:
        db.add_all([
            Employee(
                first_name="Alice",
                last_name="Smith",
                department="Engineering",
                position="Software Engineer",
                location="Remote",
                status="Active"
            ),
            Employee(
                first_name="Bob",
                last_name="Johnson",
                department="HR",
                position="HR Manager",
                location="New York",
                status="Active"
            )
        ])
        db.commit()
    db.close()