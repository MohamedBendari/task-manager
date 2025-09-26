class Task:
    def __init__(self, title, description, due_date, status, type_task):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.type_task = type_task
    def to_dict(self):
        return {
            "type": self.type_task,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }
    def tasktype(self):
        return self.type_task
