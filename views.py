from flask import Blueprint, render_template, request, redirect, abort
from models import EmployeeModel
from app import db
from commands import get_new_employee

# Creating a blueprint (route collection)
app = Blueprint("views", __name__)


# Create record
@app.route("/data/create", methods=["GET", "POST"])
def create():
    # Get create page with form
    if request.method == "GET":
        return render_template("create_page.html")

    # Fill form to create record
    if request.method == "POST":
        employee = get_new_employee(id_in_form=True)

        # Add created instance to db
        db.session.add(employee)
        db.session.commit()

        # Redirect user to data page
        return redirect("/data")


# Get list of records
@app.route("/data")
def retrieve_data_list():
    # Query all records in db as a list
    employees = EmployeeModel.query.all()

    return render_template("data_list.html", employees=employees)


# Show record
@app.route("/data/<int:id>")
def retrieve_employee(id):
    # Filter record by employee id
    employee = EmployeeModel.query.filter_by(employee_id=id).first()

    if employee:
        # If referred record exists
        return render_template("data.html", employee=employee)

    return f"Employee with id ={id} Does not exist"


# Update record by employee id
@app.route("/data/<int:id>/update", methods=["GET", "POST"])
def update(id):
    # Filter record by employee id
    employee = EmployeeModel.query.filter_by(employee_id=id).first()

    if request.method == "POST":
        # If referred record exists
        if employee:
            db.session.delete(employee)
            db.session.commit()

            # Create employee instance
            employee = get_new_employee()

            # Add created instance to db
            db.session.add(employee)
            db.session.commit()

            return redirect(f"/data/{employee.employee_id}")

        return f"Employee with id = {employee.employee_id} Does nit exist"

    return render_template("update.html", employee=employee)


@app.route("/data/<int:id>/delete", methods=["GET", "POST"])
def delete(id):
    # Filter record by employee id
    employee = EmployeeModel.query.filter_by(employee_id=id).first()

    if request.method == "POST":
        # If referred record exists
        if employee:
            # Delete record from db
            db.session.delete(employee)
            db.session.commit()

            return redirect("/data")

        abort(404)

    return render_template("delete.html")
