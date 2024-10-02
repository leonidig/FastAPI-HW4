from os import getenv
from requests import get
from flask import render_template
from flask_login import current_user, login_required
from .. import app


BACKEND_URL = getenv("BACKEND_URL")


@app.get("/")
@login_required
def index():
    email = current_user.email
    data = {
        "email": email
    }
    tasks = {
        "tasks": get(f"{BACKEND_URL}/read", json=data).json()
    }
    # print(tasks)
    # print(data.get("email"))
    nickname = email.split("@")[0]
    return render_template("index.html", **tasks, nickname=nickname) 