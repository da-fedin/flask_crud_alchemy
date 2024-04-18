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


@app.route("/data")
def retrieve_data_list():
    employees = EmployeeModel.query.all()
    return render_template("data_list.html", employees=employees)
