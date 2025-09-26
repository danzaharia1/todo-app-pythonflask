from flask import Flask, jsonify, request
from data_service import get_all_todos, toggle_todo

app = Flask(__name__)

# Route to get all todos (Read operation)
@app.route('/todos', methods=['GET'])
def list_todos():
    todos = get_all_todos()
    # ERROR: Cannot directly jsonify a list of custom Todo objects.
    # This will force the user to go back to models.py and add the to_dict method
    # or iterate through the list to convert them.
    return jsonify(todos)

# Route to toggle the completion status of a todo item (Update operation)
@app.route('/todos/toggle/<int:todo_id>', methods=['POST'])
def toggle_completion_route(todo_id):
    if toggle_todo(todo_id):
        return jsonify({"message": f"Todo {todo_id} toggled successfully"}), 200
    return jsonify({"error": "Todo not found"}), 404

if __name__ == '__main__':
    # Running in debug mode for easy testing (common in VSCode dev setup)
    app.run(debug=True)