from task import Task

class PersonalTask(Task):
    def __init__(self, title, description, due_date, status, category, type_task):
        super().__init__(title, description, due_date, status, type_task)
        self.category = category

    def to_dict(self):
        data = super().to_dict()
        data["category"] = self.category
        return data
