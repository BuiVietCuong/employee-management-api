from fastapi import FastAPI
from .employee_management.routers.employee.api import router as employee_api_router

app = FastAPI()

# Include all API routes under root or a prefix
app.include_router(employee_api_router)