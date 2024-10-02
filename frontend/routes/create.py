from os import getenv
from requests import post
from flask import (render_template,
                   request,
                   url_for,
                   redirect)
from flask_login import login_required, current_user
from .. import app


BACKEND_URL = getenv("BACKEND_URL")

@app.get("/create")
@login_required
def get_create():
    return render_template("create.html")


@app.post("/create")
def get_data():
    content = request.form.get("content")
    user = current_user.email
    data = {
        "content": content,
        "author": user
    }
    response = post(f'{BACKEND_URL}/create', json=data)
    if response.status_code == 200:
        return redirect(url_for("index"))
    else: 
        return f"Error: {response.status_code}"
