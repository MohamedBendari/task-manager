import json
from task import Task
from personal_task import PersonalTask
from work_task import WorkTask
from task_manager import TaskManager

manager = TaskManager()

try:
    with open("data.json", "r") as f:
        tasks_data = json.load(f)
        for t in tasks_data:
            if "priority" in t:                           
                task = WorkTask(
                    t["title"], t["description"], t["due_date"], t["status"], t["priority"], t["type"]
                )
            elif "category" in t:                        
                task = PersonalTask(
                    t["title"], t["description"], t["due_date"], t["status"], t["category"], t["type"]
                )
            manager.add_task(task)
except FileNotFoundError:
    print("No previous data")

while True:
    print("================= Task Manager =================")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Show Tasks")
    print("4. Update Due Date")
    print("5. Mark Task as Completed")
    print("6. Mark Task as in progress")
    print("7. Quit")

    choice = input("please enter your choice : ")

    try:
        if choice == "1":
            while True:
                the_type = input("Enter the task type: ").lower()
                if the_type=="work" or the_type=="personal":
                    break
                else:
                    print("Invalid type. Please enter 'work' or 'personal'.")
            title = input("title: ")
            found = False
            for t in manager.tasks:
                if t.title.lower() == title.lower():
                    found = True
                    break
            if found:
                print(f"the task title '{title}' is already exists. Please choose another title.")
                continue  
            description = input("Description: ")
            due_date = input("Due Date: ")
            status = "incomplete"
            if the_type == "work":
                priority = input("Priority: ")
                task = WorkTask(title, description, due_date, status, priority, "work")

            elif the_type == "personal":
                category = input("Category: ")
                task = PersonalTask(title, description, due_date, status, category, "personal")
            manager.add_task(task)

        elif choice == "2":
            title = input("Enter the title to delete: ")
            manager.delete_task(title)

        elif choice == "3":
            manager.list_tasks()

        elif choice == "4":
            title = input("Enter task title: ")
            new_due = input("Enter new due date : ")
            manager.update_due_date(title, new_due)

        elif choice == "5":
            title = input("Enter task title to mark as completed: ")
            manager.mark_completed(title)
        elif choice == "6":
            title = input("Enter task title to mark as in progress: ")
            manager.mark_inprogress(title)
        elif choice == "7":
            print("Goodbye")
            break

        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Error")
