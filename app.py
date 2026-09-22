# app.py
import os
from flask import Flask, request
from db import db
from repo import ItemRepository
from flask import jsonify


app = Flask(__name__)

# Fetch the variables from your .env file safely
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")

# Dynamically construct the MySQL URI
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route("/")
def home():
    return {"message": "Welcome to Item Management", "status": "success"}

@app.get("/item")
def get_all():
    items = ItemRepository.get_all()
    return [item.to_dict() for item in items], 200


@app.get("/item/<int:item_id>")
def get_one(item_id):
    item = ItemRepository.get_by_id(item_id)
    if not item:
        return {"error" : f"Item with id {item_id} not found"}, 404
    else:
        return item.to_dict()
    
    
    
@app.post("/item")
def create_one():
    data = request.get_json()
    if not data or "name" not in data or "price" not in data:
        return {"error" : "Missing fields in request"}, 400
    new_item = ItemRepository.create(data['name'], data['price'])
    return new_item.to_dict(), 201


@app.delete("/item/<int:id>")
def delete_item(id):
    if ItemRepository.delete(id):
        return {"message" : "item deleted"}, 200
    else:
        return {"error" : f"Item not found with id: {id}"}, 404
    
    
@app.patch("/item/<int:id>")
def update_item(id):
    item = ItemRepository.get_by_id(id)
    if not item:
        return {"error" : f"Item not found with id: {id}"}, 404
    data = request.get_json()
    if not data or "name" not in data or "price" not in data:
        return {"error" : "Missing fields in request"}, 400
    updated_item = ItemRepository.update(id, data["name"], data["price"])
    return updated_item.to_dict(), 202