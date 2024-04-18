from flask import Blueprint, render_template, request, redirect
from models import EmployeeModel
from app import db

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
        employee_id = request.form["employee_id"]
        name = request.form["name"]
        age = request.form["age"]
        position = request.form["position"]

        # Create employee instance
        employee = EmployeeModel(
            employee_id=employee_id, name=name, age=age, position=position
        )

        # Add created instance to db
        db.session.add(employee)
        db.session.commit()

        # Redirect user to data page
        return redirect("/data")


# Get data list
@app.route("/data")
def retrieve_data_list():
    # Query all data in db as a list
    employees = EmployeeModel.query.all()

    return render_template("data_list.html", employees=employees)


@app.route("/data/<int:id>")
def retrieve_employee(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if employee:
        return render_template("data.html", employee=employee)
    return f"Employee with id ={id} Does not exist"


@app.route("/data/<int:id>/update", methods=["GET", "POST"])
def update(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == "POST":
        if employee:
            db.session.delete(employee)
            db.session.commit()
            name = request.form["name"]
            age = request.form["age"]
            position = request.form["position"]
            employee = EmployeeModel(
                employee_id=id, name=name, age=age, position=position
            )
            db.session.add(employee)
            db.session.commit()
            return redirect(f"/data/{id}")
        return f"Employee with id = {id} Does nit exist"

    return render_template("update.html", employee=employee)


@app.route("/data/<int:id>/delete", methods=["GET", "POST"])
def delete(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()

    if request.method == "POST":
        if employee:
            db.session.delete(employee)
            db.session.commit()

            return redirect("/data")
        # abort(404)    # :TODO: fix

    return render_template("delete.html")
