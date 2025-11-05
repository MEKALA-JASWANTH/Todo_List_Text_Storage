import tkinter as tk
from tkinter import messagebox, simpledialog
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List Manager - By Jaswanth")
        self.root.geometry("600x500")
        self.root.config(bg="#f0f0f0")
        
        self.tasks_file = "tasks.txt"
        self.tasks = []
        
        # Create GUI components
        self.create_widgets()
        
        # Load tasks from file
        self.load_tasks()
        
    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self.root, text="Todo List Manager", 
                              font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=10)
        
        # Frame for task input
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=10)
        
        self.task_entry = tk.Entry(input_frame, width=40, font=("Arial", 12))
        self.task_entry.grid(row=0, column=0, padx=5)
        
        add_button = tk.Button(input_frame, text="Add Task", command=self.add_task,
                              bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        add_button.grid(row=0, column=1, padx=5)
        
        # Frame for task listbox
        list_frame = tk.Frame(self.root, bg="#f0f0f0")
        list_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        # Scrollbar for listbox
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox = tk.Listbox(list_frame, width=50, height=12, 
                                       font=("Arial", 11), yscrollcommand=scrollbar.set)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Frame for buttons
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)
        
        mark_button = tk.Button(button_frame, text="Mark Complete", command=self.mark_complete,
                               bg="#2196F3", fg="white", font=("Arial", 10, "bold"), width=15)
        mark_button.grid(row=0, column=0, padx=5, pady=5)
        
        edit_button = tk.Button(button_frame, text="Edit Task", command=self.edit_task,
                               bg="#FF9800", fg="white", font=("Arial", 10, "bold"), width=15)
        edit_button.grid(row=0, column=1, padx=5, pady=5)
        
        delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task,
                                 bg="#f44336", fg="white", font=("Arial", 10, "bold"), width=15)
        delete_button.grid(row=0, column=2, padx=5, pady=5)
        
        # Statistics frame
        stats_frame = tk.Frame(self.root, bg="#e0e0e0", relief=tk.RAISED, borderwidth=2)
        stats_frame.pack(pady=10, padx=20, fill=tk.X)
        
        self.total_label = tk.Label(stats_frame, text="Total Tasks: 0", 
                                   font=("Arial", 11, "bold"), bg="#e0e0e0")
        self.total_label.grid(row=0, column=0, padx=20, pady=5)
        
        self.completed_label = tk.Label(stats_frame, text="Completed: 0", 
                                       font=("Arial", 11, "bold"), bg="#e0e0e0")
        self.completed_label.grid(row=0, column=1, padx=20, pady=5)
        
        self.pending_label = tk.Label(stats_frame, text="Pending: 0", 
                                     font=("Arial", 11, "bold"), bg="#e0e0e0")
        self.pending_label.grid(row=0, column=2, padx=20, pady=5)
        
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            task_item = {"task": task, "completed": False}
            self.tasks.append(task_item)
            self.update_listbox()
            self.save_tasks()
            self.task_entry.delete(0, tk.END)
            self.update_statistics()
        else:
            messagebox.showwarning("Input Error", "Please enter a task!")
    
    def mark_complete(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = not self.tasks[selected_index]["completed"]
            self.update_listbox()
            self.save_tasks()
            self.update_statistics()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark!")
    
    def edit_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            current_task = self.tasks[selected_index]["task"]
            new_task = simpledialog.askstring("Edit Task", "Edit your task:", initialvalue=current_task)
            if new_task:
                self.tasks[selected_index]["task"] = new_task.strip()
                self.update_listbox()
                self.save_tasks()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to edit!")
    
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task_name = self.tasks[selected_index]["task"]
            confirm = messagebox.askyesno("Delete Task", f"Are you sure you want to delete: '{task_name}'?")
            if confirm:
                self.tasks.pop(selected_index)
                self.update_listbox()
                self.save_tasks()
                self.update_statistics()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete!")
    
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["completed"] else "○"
            display_text = f"{status} {task['task']}"
            self.task_listbox.insert(tk.END, display_text)
            if task["completed"]:
                # Highlight completed tasks
                self.task_listbox.itemconfig(tk.END, fg="green")
    
    def save_tasks(self):
        with open(self.tasks_file, "w") as file:
            for task in self.tasks:
                status = "DONE" if task["completed"] else "TODO"
                file.write(f"{status}|{task['task']}\n")
    
    def load_tasks(self):
        if os.path.exists(self.tasks_file):
            with open(self.tasks_file, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split("|", 1)
                        if len(parts) == 2:
                            status, task = parts
                            task_item = {
                                "task": task,
                                "completed": status == "DONE"
                            }
                            self.tasks.append(task_item)
            self.update_listbox()
            self.update_statistics()
    
    def update_statistics(self):
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task["completed"])
        pending = total - completed
        
        self.total_label.config(text=f"Total Tasks: {total}")
        self.completed_label.config(text=f"Completed: {completed}")
        self.pending_label.config(text=f"Pending: {pending}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
