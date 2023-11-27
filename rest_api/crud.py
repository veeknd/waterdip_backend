from sqlalchemy.orm import Session
from typing import List

from . import models, schemas

def create_task(db:Session, task: schemas.TaskBase):
    db_task = models.Task(title= task.title, is_completed= task.is_completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db:Session, skip: int = 0, limit: input = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def delete_task(db:Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    db.delete(db_task)
    db.commit()
    return db_task

def update_task(db:Session, task_id: int, title: str , is_completed: bool):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    db_task.title = title
    db_task.is_completed = is_completed
    db.commit()
    return db_task

def create_tasks(db:Session, tasks: List[schemas.TaskBase]):
    lis = []
    for task in tasks:
        task_created = create_task(db, task)
        lis.append({'id':task_created.id})
    return lis



