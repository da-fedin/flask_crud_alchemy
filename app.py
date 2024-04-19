import os

from flask import Flask
from models import db
from views import app as views_app
from commands import initialize_services

# Initialize the flask app
app = Flask(__name__)

# Link SQLite DB with SQLAlchemy
db_path = os.path.join(os.path.dirname(__file__), "db", "db.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the db instance
db.init_app(app)

# Registering the views from views.py
app.register_blueprint(views_app)

with app.app_context():
    db.create_all()


@app.before_request
def initialize_app() -> None:
    # Perform initialization tasks here
    print("Flask app is starting up")

    initialize_services()


if __name__ == "__main__":
    app.run(debug=True)
