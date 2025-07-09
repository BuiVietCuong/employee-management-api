FROM python:3.11-slim

# Environment config
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system packages (optional, for building some wheels)
RUN apt-get update && apt-get install -y build-essential

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY ./src ./src

# Expose app port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "employee_management_api.employee_management.app:app", "--host", "0.0.0.0", "--port", "8000"]