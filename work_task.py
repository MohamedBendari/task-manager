from task import Task

class WorkTask(Task):
    def __init__(self, title, description, due_date, status, priority, type_task):
        super().__init__(title, description, due_date, status, type_task)
        self.priority = priority

    def to_dict(self):
        data = super().to_dict()
        data["priority"] = self.priority
        return data
