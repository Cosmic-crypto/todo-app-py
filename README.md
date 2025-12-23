# 📝 Streamlit Todo App

A simple todo list web application built with **Python** and **Streamlit**.  
This app allows users to add tasks, mark them as completed, delete them, and **persist tasks between sessions** using a JSON file.

---

## 🚀 Features

- ➕ Add new tasks  
- ✅ Mark tasks as completed  
- ❌ Delete tasks  
- 💾 Automatic saving (tasks persist after refresh/restart)  
- 🖥 Simple and clean web UI  
- ⚡ Lightweight (no database required)

---

## 🛠 Tech Stack

- **Python 3**
- **Streamlit**
- **JSON** (for data persistence)

---

## 📂 Project Structure



.
├── todo_app.py # Main Streamlit application
├── tasks.json # Saved tasks (auto-created)
└── README.md # Project documentation


---

## 📦 Installation

1. Clone or download the repository  
2. Install Streamlit:



pip install streamlit


---

## ▶️ Running the App

From the project directory:



streamlit run todo_app.py


Your browser will automatically open the app.

---

## 🧠 How It Works

### Streamlit Rerun Model

- Streamlit reruns the script **top to bottom** on every user interaction.
- To keep data between reruns, the app uses `st.session_state`.

### Task Structure

Each task is stored as a dictionary:



{
"text": "Buy milk",
"done": false
}


All tasks are stored in a list:



st.session_state.tasks


---

## 💾 Data Persistence

- Tasks are saved to `tasks.json`
- Tasks automatically load when the app starts
- This ensures tasks are not lost after refreshing or restarting the app

---

## 🧩 Key Concepts Used

- `st.session_state` – persistent app memory  
- `st.text_input()` – user input  
- `st.button()` – actions  
- `st.checkbox()` – task completion  
- `st.columns()` – layout control  
- `json` – saving/loading tasks  
- `st.rerun()` – clean UI refresh after updates  

---

## 🧪 Example Workflow

1. User types a task  
2. Clicks **Add**  
3. Task is added to session state  
4. Tasks are saved to `tasks.json`  
5. App reruns and updates the UI  

---

## 🔮 Possible Improvements

- 📅 Due dates  
- ⭐ Task priorities  
- 🔍 Search & filtering  
- 🗄 SQLite database support  
- 👥 Multi-user functionality  
- ☁ Deployment to Streamlit Cloud  

---

## 📄 License

This project is open-source and free to use for learning and personal projects.
