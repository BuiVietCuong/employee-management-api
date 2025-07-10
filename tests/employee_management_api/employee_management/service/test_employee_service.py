# tests/employee_management_api/employee_management/services/test_employee_service.py

import pytest
from unittest.mock import MagicMock
from employee_management_api.employee_management.services import employee_service
from employee_management_api.employee_management.models.employee import Employee


def test_get_employees_by_status():
    mock_session = MagicMock()
    mock_repo = MagicMock()

    mock_repo.get_employees.return_value = [
        Employee(first_name="John", last_name="Doe", position="Engineer", status="active"),
        Employee(first_name="Jane", last_name="Smith", position="Manager", status="active"),
    ]

    result = employee_service.get_employees(
        db=mock_session,
        repo=mock_repo,
        filters={"status": ["active"]},
        organization_id="orgA"
    )

    assert len(result) == 2
    assert result[0].first_name == "John"
