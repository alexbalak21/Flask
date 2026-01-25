from flask import Blueprint, request, jsonify
from repository.todo_repository import TodoRepository

todo_bp = Blueprint('todo', __name__, url_prefix='/api/todos')

@todo_bp.route('/', methods=['GET'])
def get_all_todos():
    """Get all todos"""
    todos = TodoRepository.get_all()
    return jsonify([todo.to_dict() for todo in todos]), 200

@todo_bp.route('/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Get a single todo by ID"""
    todo = TodoRepository.get_by_id(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify(todo.to_dict()), 200

@todo_bp.route('/', methods=['POST'])
def create_todo():
    """Create a new todo"""
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    title = data['title']
    completed = data.get('completed', False)
    
    todo = TodoRepository.create(title=title, completed=completed)
    return jsonify(todo.to_dict()), 201

@todo_bp.route('/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update an existing todo"""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    title = data.get('title')
    completed = data.get('completed')
    
    todo = TodoRepository.update(todo_id, title=title, completed=completed)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    
    return jsonify(todo.to_dict()), 200

@todo_bp.route('/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo"""
    success = TodoRepository.delete(todo_id)
    if not success:
        return jsonify({'error': 'Todo not found'}), 404
    
    return jsonify({'message': 'Todo deleted successfully'}), 200
