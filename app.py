from flask import Flask
from models import db
from views import app as views_app

# Initialize the flask app
app = Flask(__name__)

# Link SQLite DB with SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///<db_name>.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the db instance
db.init_app(app)

# Registering the views from views.py
app.register_blueprint(views_app)


# Create DB file before the user accesses the server
# @app.before_first_request
# def create_table():
#     db.create_all()
with app.app_context():
    db.create_all()

app.run(host="localhost", port=5000)
