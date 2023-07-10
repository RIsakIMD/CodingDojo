
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

@app.route('/users/<int:user_id>/')
def show(user_id):
    return render_template("single_user.html", user=User.get_one(user_id))

@app.route('/users/<int:user_id>/edit/')
def edit(user_id):
    return render_template("edit.html", user=User.get_one(user_id))

@app.route('/users/<int:user_id>/edit/submit/', methods=['POST'])
def edit_submit(user_id):
    data = {
        "id" : user_id,
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.edit_user(data)
    return redirect(f'/users/{user_id}')

@app.route('/users/<int:user_id>/delete/')
def delete(user_id):
    User.delete_user({"id": user_id})
    return redirect('/')