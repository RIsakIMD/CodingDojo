
from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.users import User

@app.route('/')
def root():
    return render_template("read.html", users=User.get_all())

@app.route('/create/')
def create():
    return render_template("create.html")

@app.route('/submit/', methods=['POST'])
def submit():
    User.add_user(request.form)
    return redirect('/')