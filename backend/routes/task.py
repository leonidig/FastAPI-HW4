from sqlalchemy import (select,
                        and_,
                        update)
from fastapi import HTTPException
from main import app
from db import (Session,
                Task)
from schemas import (CreateTask,
                     ReadTask,
                     TaskData,
                     TaskInfo,
                     TaskDelete)


@app.get("/read")
def read(data: ReadTask):
    with Session.begin() as session:
        tasks = session.scalars(select(Task).where(Task.author == data.email)).all()
        tasks = [TaskData.model_validate(task) for task in tasks]
        return tasks 


@app.post('/create')
def create(data: CreateTask):
    with Session.begin() as session:
        task = Task(**data.model_dump())
        session.add(task)
        return task
    

@app.get("/task/{task_id}")
def get_task(task_id):
    with Session.begin() as session:
        task = session.scalar(select(Task).where(Task.id == task_id))
        task = TaskData.model_validate(task)
        return task



@app.delete("/delete/{task_id}")
def delete_task(data: TaskDelete):
    with Session.begin() as session:
        task = session.scalar(select(Task).where(Task.id == data.task_id))
        if task.author != data.user:
            return "hahah loh" 
        if task:
            session.delete(task)



@app.put("/edit_task")
def edit_task(data: TaskData):
    with Session.begin() as session:
        task = session.scalar(select(Task).where(Task.id == data.id))
        if task.author != data.author:
            raise HTTPException(status_code=403, detail="Permission denied")
        upd = update(Task).where(Task.id == data.id).values(
            content=data.content,
        )
        session.execute(upd)
        return task