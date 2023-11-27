from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/v1/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskBase, db:Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@app.post("/v1/taskss/", response_model=None)
def create_tasks(task: List[schemas.TaskBase], db:Session = Depends(get_db)):
    return crud.create_tasks(db=db, tasks=task)

@app.get("/v1/tasks/", response_model=List[schemas.Task])
def read_tasks(skip: int =0, limit: int =100, db: Session = Depends(get_db)):
    Tasks = crud.get_tasks(db, skip=skip,limit=limit)
    return Tasks

@app.get("/v1/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return db_task

@app.delete("/v1/tasks/{task_id}",status_code=204, response_model=None)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return None

    

@app.put("/v1/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int,  title: str, is_completed: bool, db: Session = Depends(get_db)):
    db_task = crud.update_task(db, task_id=task_id ,title=title, is_completed=is_completed)
    if db_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return db_task

