from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

# Create hub for database operations within the application
db = SQLAlchemy()


class EmployeeModel(db.Model):
    """Model to represent a table in a database"""

    # Set the name of the table in the database
    __tablename__ = "table"

    # Define columns
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(), unique=True, nullable=False)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))

    def __init__(self, employee_id, name, age, position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return f"{self.employee_id}: {self.name}, {self.age}, {self.position}"

    @validates("employee_id")
    def validate_employee_id(self, key, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")

        return value

    @validates("age")
    def validate_employee_age(self, key, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")

        return value
