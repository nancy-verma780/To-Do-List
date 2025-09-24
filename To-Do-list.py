class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"Added task: {task}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        for idx, t in enumerate(self.tasks, start=1):
            status = "✔" if t["done"] else "✖"
            print(f"{idx}. [{status}] {t['task']}")

    def mark_done(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]["done"] = True
            print(f"Marked task #{index} as done.")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"Deleted task #{index}: {removed['task']}")
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            print("\n--- To-Do Menu ---")
            print("1. Add task")
            print("2. List tasks")
            print("3. Mark task as done")
            print("4. Delete task")
            print("5. Exit")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                task = input("Enter task description: ").strip()
                if task:
                    self.add_task(task)
                else:
                    print("Cannot add empty task.")
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                num = input("Enter task number to mark done: ").strip()
                if num.isdigit():
                    self.mark_done(int(num))
                else:
                    print("Please enter a valid number.")
            elif choice == "4":
                num = input("Enter task number to delete: ").strip()
                if num.isdigit():
                    self.delete_task(int(num))
                else:
                    print("Please enter a valid number.")
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    app = ToDoList()
    app.run()
