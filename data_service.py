from models import Todo

# Initial data set - missing the 'due_date'
_todos = [
    Todo(1, "Review design mocks", False),
    Todo(2, "Set up user research session for code prediction feature", False),
    Todo(3, "Draft technical spec for new shopping cart API", True),
    Todo(4, "Prepare performance review doc for 1:1 with Kate", False),
]

def get_all_todos():
    """Returns the entire list of Todos."""
    return _todos

def toggle_todo(todo_id):
    """Toggles the completion status of a single todo item."""
    for todo in _todos:
        if todo.id == todo_id:
            todo.toggle_completion()
            return True
    return False
