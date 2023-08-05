import tkinter as tk
from tkinter import messagebox
import json

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TaskOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Organizer")
        self.root.geometry("500x400")  # Set the window size

        self.tasks = []

        self.load_tasks()

        self.create_widgets()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        self.task_label = tk.Label(self.root, text="New Task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack()

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)

        self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.complete_task)
        self.complete_button.pack()

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.update_task_list()

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)
                self.tasks = [Task(task_data["description"], task_data["completed"]) for task_data in data]
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            data = [{"description": task.description, "completed": task.completed} for task in self.tasks]
            json.dump(data, file)

    def add_task(self):
        description = self.task_entry.get()
        if description:
            new_task = Task(description)
            self.tasks.append(new_task)
            self.save_tasks()
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task.completed = not task.completed
            self.save_tasks()
            self.update_task_list()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.save_tasks()
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓ " if task.completed else "[ ] "
            self.task_listbox.insert(tk.END, status + task.description)

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()

def main():
    root = tk.Tk()
    app = TaskOrganizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
