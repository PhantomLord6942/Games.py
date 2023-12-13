import tkinter as tk
from tkinter import StringVar, ttk
from collections import defaultdict



from collections import defaultdict

test = defaultdict(list)
print(test)

root = tk.Tk()
root.title("To-Do List")

tasks = []

task_entry = ttk.Entry(root)
task_entry.grid(row=0, column=1)


def add_task():
    task = task_entry.get()
    tasks.append(task)
    task_list.insert(tk.END, task)
    task_entry.delete(0, tk.END)


add_btn = ttk.Button(root, text="Add Task", command=add_task)
add_btn.grid(row=0, column=0)

task_list = tk.Listbox(root)
task_list.grid(row=1, column=0, columnspan=2)


def delete_task():
    task = task_list.get(tk.ANCHOR)
    tasks.remove(task)
    task_list.delete(tk.ANCHOR)


delete_btn = ttk.Button(root, text="Delete", command=delete_task)
delete_btn.grid(row=2, column=0)

import json

# Load tasks from file on startup
try:
    with open('tasks.json') as f:
        tasks = json.load(f)
except:
    pass

# Save tasks to file on exit
def save_tasks():
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

root.protocol("WM_DELETE_WINDOW", save_tasks)


# Add boolean completed field
tasks = [{'text':'Sample task', 'completed':False}]

# Checkmark sign for completed
def mark_completed(idx):
    tasks[idx]['completed'] = True
    task_list.itemconfig(idx, text='✔️' + tasks[idx]['text'])

task_list.bind('<Button-1>', mark_completed)

edit_entry = ttk.Entry(root)

def edit_task():
    task = task_list.get(tk.ANCHOR)
    edit_entry.insert(0, task)
    edit_entry.grid(row=0, column=1)

edit_btn = ttk.Button(root, text="Edit", command=edit_task)
edit_btn.grid(row=2, column=1)

def save_edit():
    task = edit_entry.get()
    tasks[task_list.index(tk.ANCHOR)]['text'] = task
    task_list.delete(tk.ANCHOR)
    task_list.insert(tk.ANCHOR, task)
    edit_entry.grid_remove()

edit_entry.bind("<FocusOut>", save_edit)


import calendar

# Dictionary to store tasks by date
tasks_by_date = defaultdict(list)

def show_calendar():
    # Create calendar
    cal = calendar.month(2023, 2)

    # Display tasks under dates
    for date, tasks in tasks_by_date.items():
        cal += f"\n{date}:\n"
        for task in tasks:
            cal += f"- {task}\n"

    print(cal)

show_calendar()



from datetime import date

# Task dict with due date
tasks = [{'text':'Do laundry', 'due': date(2023, 3, 1)}]

# Sort tasks by due date
tasks.sort(key=lambda t: t['due'])

# Display due date in calendar
for date, tasks in tasks_by_date.items():
    for task in tasks:
        due = task['due'].strftime("%b %d")
        cal += f"- {task['text']} (Due {due})\n"

from collections import defaultdict


# Other code

def show_calendar():
    tasks_by_date = defaultdict(list)

    # Rest of calendar code


root.mainloop()
