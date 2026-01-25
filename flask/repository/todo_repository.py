from model.todo import Todo, db

class TodoRepository:
    
    @staticmethod
    def get_all():
        """Get all todos"""
        return Todo.query.all()
    
    @staticmethod
    def get_by_id(todo_id):
        """Get a todo by ID"""
        return Todo.query.get(todo_id)
    
    @staticmethod
    def create(title, completed=False):
        """Create a new todo"""
        todo = Todo(title=title, completed=completed)
        db.session.add(todo)
        db.session.commit()
        return todo
    
    @staticmethod
    def update(todo_id, title=None, completed=None):
        """Update an existing todo"""
        todo = Todo.query.get(todo_id)
        if not todo:
            return None
        
        if title is not None:
            todo.title = title
        if completed is not None:
            todo.completed = completed
        
        db.session.commit()
        return todo
    
    @staticmethod
    def delete(todo_id):
        """Delete a todo by ID"""
        todo = Todo.query.get(todo_id)
        if not todo:
            return False
        
        db.session.delete(todo)
        db.session.commit()
        return True
