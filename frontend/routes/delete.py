from os import getenv
from flask_login import (current_user,
                         login_required)
from flask import (render_template,
                   request,
                   redirect,
                   url_for)
from requests import delete
from .. import app


BACKEND_URL = getenv("BACKEND_URL")


@app.get("/delete/<int:task_id>")
@login_required
def delete_validation(task_id):
    return render_template("delete.html", task_id=task_id)


@app.post("/delete/<int:task_id>")
def delete_task(task_id):
    response = request.form.get("response")
    if response == "yes":
        data = {
            "task_id": task_id,
            "user": current_user.email
        }
        response = delete(f"{BACKEND_URL}/delete/{task_id}", json=data)
        if response.status_code == 200:
            return redirect(url_for("index"))
        else:
            print(f"Error - {response.status_code}")
    else:
        return redirect(url_for("index"))