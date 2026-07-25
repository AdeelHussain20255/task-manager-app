from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
import database

# Initialize FastAPI app
app = FastAPI(title="Task Manager API")

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Pydantic Schemas for Validation ---
class TaskBase(BaseModel):
    # min_length=1 strictly rejects empty task titles
    title: str = Field(..., min_length=1, description="Task title cannot be empty")
    description: str | None = ""

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length=1)
    description: str | None = None
    is_complete: bool | None = None

class TaskResponse(TaskBase):
    id: int
    is_complete: bool

    class Config:
        from_attributes = True

# --- API Endpoints ---

# Serve the frontend UI at the root URL
@app.get("/")
def read_root():
    return FileResponse("index.html")

# Create a task (POST)
@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = database.Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Read all tasks (GET)
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(database.Task).all()

# Update a task (PUT)
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(database.Task).filter(database.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    update_data = task_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
        
    db.commit()
    db.refresh(db_task)
    return db_task

# Delete a task (DELETE)
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(database.Task).filter(database.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted successfully"}
