# Task Manager Web App

A full-stack Task Manager web application built as part of the iCodeGuru Week 3 Module Project. It allows users to seamlessly add, edit, complete, and delete tasks with persistent storage.

## 🚀 Live Demo
* **Live URL:** [https://task-manager-app-production-9e9c.up.railway.app](https://task-manager-app-production-9e9c.up.railway.app)

---

## 🛠️ Tech Stack
* **Back End:** FastAPI, SQLAlchemy, SQLite
* **Front End:** HTML5, CSS3, Vanilla JavaScript
* **Deployment:** Railway

---

## 📋 Features
* **Full CRUD Functionality:** Create, read, update/edit, mark complete/incomplete, and delete tasks.
* **Persistent Database:** Uses SQLite so your data survives page refreshes and server restarts.
* **Input Validation:** Built-in Pydantic validation on the backend to reject empty or invalid task data.

---

## 💻 Running Locally

Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/AdeelHussain20255/task-manager-app.git
cd task-manager-app
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Development Server

```bash
uvicorn main:app --reload
```

### 5. Open in Your Browser

Navigate to `http://127.0.0.1:8000` to use the application locally.
