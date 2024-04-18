from flask import request
from models import EmployeeModel


def get_new_employee() -> EmployeeModel:
    """Create a new employee"""
    employee_id = request.form["employee_id"]
    name = request.form["name"]
    age = request.form["age"]
    position = request.form["position"]

    # Create employee instance
    employee = EmployeeModel(
        employee_id=employee_id, name=name, age=age, position=position
    )

    return employee
