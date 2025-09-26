class Todo:
    def __init__(self, id, text, is_completed):
        self.id = id
        self.text = text
        self.is_completed = is_completed

    def toggle_completion(self):
        self.is_completed = not self.is_completed

    # add a method like to_dict() here for JSON serialization
    # and update the __init__ and toggle_completion methods.
    
    def __str__(self):
        status = "[X]" if self.is_completed else "[ ]"
        return f"{status} {self.text}"

    def __repr__(self):
        return f"Todo(id={self.id}, text='{self.text}', is_completed={self.is_completed})"