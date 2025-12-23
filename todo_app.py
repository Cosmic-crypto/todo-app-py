import streamlit as st
from json import dump, load
from os import path

st.title("📝 Todo App")

def save_tasks():
    with open("tasks.json", "w") as f:
        dump(st.session_state.tasks, f)

if "tasks" not in st.session_state:
    if path.exists("tasks.json"):
        with open("tasks.json") as f:
            st.session_state.tasks = load(f)
    else:
        st.session_state.tasks = []

new_task = st.text_input("Add a new task")

if st.button("Add"):
    if new_task.strip():
        st.session_state.tasks.append({
            "text": new_task,
            "done": False
        })
        save_tasks()
        st.rerun()

st.subheader("Your Tasks")

for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4, 1])

    checked = col1.checkbox(
        task["text"],
        value=task["done"],
        key=f"task_{i}"
    )

    task["done"] = checked

    if col2.button("❌", key=f"delete_{i}"):
        st.session_state.tasks.pop(i)
        save_tasks()
        st.rerun()