from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    __tablename__ = 'todos'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }
    
    def __repr__(self):
        return f'<Todo {self.id}: {self.title}>'
