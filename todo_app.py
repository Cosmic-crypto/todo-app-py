import streamlit as st
from json import dump, load
from os import path
from datetime import date
from notifypy import Notify

st.title("📝 Todo App")

# ------------------ Notification ------------------

def notify(title: str, message: str):
    n = Notify()
    n.title = title
    n.message = message
    n.send()

# ------------------ Persistence ------------------

def save_tasks():
    with open("tasks.json", "w") as f:
        dump(st.session_state.tasks, f)

if "tasks" not in st.session_state:
    if path.exists("tasks.json"):
        with open("tasks.json") as f:
            st.session_state.tasks = load(f)
    else:
        st.session_state.tasks = []

# ------------------ Add Task ------------------

new_task = st.text_input("Add a new task")

if st.button("Add"):
    if new_task.strip():
        st.session_state.tasks.append({
            "text": new_task,
            "done": False,
            "created": date.today().isoformat(),
            "reminded": False
        })
        save_tasks()
        notify("Task created!", new_task)
        st.rerun()

# ------------------ Reminder Logic ------------------

today = date.today()

for task in st.session_state.tasks:
    created = date.fromisoformat(task["created"])

    if not task["done"] and not task["reminded"]:
        if (today - created).days >= 1:
            notify("⏰ Reminder", f"Task pending: {task['text']}")
            task["reminded"] = True
            save_tasks()

# ------------------ Display Tasks ------------------

st.subheader("Your Tasks")

for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4, 1])

    task["done"] = col1.checkbox(
        task["text"],
        value=task["done"],
        key=f"task_{i}"
    )

    if col2.button("❌", key=f"delete_{i}"):
        st.session_state.tasks.pop(i)
        save_tasks()
        st.rerun()
