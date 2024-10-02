from os import getenv
from requests import get, post
from flask import render_template
from flask_login import current_user
from .. import app



BACKEND_URL = getenv("BACKEND_URL")



@app.get("/task/<int:task_id>")
def info(task_id):
    user = current_user.email
    data = {
        "user": user,

    }
    response = get(f"{BACKEND_URL}/task/{task_id}", json=data)
    if response.status_code == 200:
        task = response.json()
        return render_template("info.html", task=task, task_id=task_id)
    else:
        return render_template("errors.html", error_code=response.status_code, text=response.text)