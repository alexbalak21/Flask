from flask import Flask
from model.todo import db
from controller.todo_controller import todo_bp
from config import Config

app = Flask(__name__)

# Configuration
app.config.from_object(Config)

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