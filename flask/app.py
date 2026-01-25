from flask import Flask
from model.todo import db
from controller.todo_controller import todo_bp
import os
from urllib.parse import quote_plus

app = Flask(__name__)

# Configuration from environment variables
user = os.getenv('MYSQL_USER', 'root')
password = os.getenv('MYSQL_PASSWORD', '')
host = os.getenv('MYSQL_HOST', 'localhost')
port = os.getenv('MYSQL_PORT', '3306')
database = os.getenv('MYSQL_DB', 'flask')

# URL-encode password for special characters
encoded_password = quote_plus(password)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{encoded_password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Register blueprints
app.register_blueprint(todo_bp)

@app.route("/")
def hello_world():
    return "<h1>Hello from Flask!</h1>"

# Create tables
with app.app_context():
    db.create_all()