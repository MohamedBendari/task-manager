import json
from task import Task
from personal_task import PersonalTask
from work_task import WorkTask

class TaskManager:
    def __init__(self, filename="data.json"):
        self.tasks = []
        self.filename = filename

    def save_to_file(self):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=2)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_to_file() 

    def delete_task(self, title):
        title = title.lower()
        for task in self.tasks:
            if task.title.lower() == title:
                self.tasks.remove(task)
                print(f"Task '{title}' deleted.")
                self.save_to_file()  
                return
        print("Task not found.")

    def list_tasks(self):
        if self.tasks == []:
            print("No tasks available.")
        else:
            for task in self.tasks:
                if task.tasktype() == "work":                          
                    print(f" task: {task.title} , {task.description} , Due: {task.due_date} , Status: {task.status} , Type: {task.tasktype()} , Priority: {task.priority}")
                elif task.tasktype() == "personal":                      
                    print(f" task: {task.title} , {task.description} , Due: {task.due_date} , Status: {task.status} , Type: {task.tasktype()} , Category: {task.category}")
    def mark_inprogress(self, title):
        title = title.lower()
        for task in self.tasks:
            if task.title.lower() == title:
                task.status = "in progress"
                print("Task is in progress")
                self.save_to_file()
                return
            
        print("Task not found.") 
    def mark_completed(self, title):
        title = title.lower()
        for task in self.tasks:
            if task.title.lower() == title:
                task.status = "completed"
                print("Task marked as completed.")
                self.save_to_file()
                return
            
        print("Task not found.")                  

    def update_due_date(self, title, new_due_date):
        title = title.lower()
        for task in self.tasks:
            if task.title.lower() == title:
                task.due_date = new_due_date
                print("Due date updated.")
                self.save_to_file()  
                return
            
        print("Task not found.")                                
