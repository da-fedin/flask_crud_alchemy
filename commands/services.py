from flask import request
from models import EmployeeModel


def get_last_employee_id():  # :TODO: add clear and auto-fill commands
    # Query the maximum employee_id from the EmployeeModel table
    employee_list = EmployeeModel.query.all()

    if employee_list:
        max_employee_id = (
            EmployeeModel.query.with_entities(EmployeeModel.employee_id)
            .order_by(EmployeeModel.employee_id.desc())
            .first()
        )

    else:
        max_employee_id = [0]

    # max_employee_id is a tuple, so extract the value from it
    last_employee_id = max_employee_id[0]

    return last_employee_id


def get_new_employee(id_in_form=False) -> EmployeeModel:
    """Create a new employee"""
    if id_in_form:
        employee_id = request.form["employee_id"]

    else:
        last_employee_id = get_last_employee_id()
        employee_id = last_employee_id + 1

    name = request.form["name"]
    age = request.form["age"]
    position = request.form["position"]

    # Create employee instance
    employee = EmployeeModel(
        employee_id=employee_id, name=name, age=age, position=position
    )

    print(f"--- Employee {employee_id} ---")

    return employee
