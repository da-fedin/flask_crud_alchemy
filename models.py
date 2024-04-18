from flask_sqlalchemy import SQLAlchemy

# Create hub for database operations within the application
db = SQLAlchemy()


class EmployeeModel(db.Model):
    """Model to represent a table in a database"""

    # Set the name of the table in the database
    __tablename__ = "table"

    # Define columns
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(), unique=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))

    def __init__(self, employee_id, name, age, position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return f"{self.employee_id}: {self.name}, {self.age}, {self.position}"
