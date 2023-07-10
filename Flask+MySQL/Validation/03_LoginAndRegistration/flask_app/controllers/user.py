import re
from flask import render_template, request, redirect, flash, session
from flask_app import app
from flask_app.models.user import User

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

@app.route('/')
def root():
    return render_template("root.html")

@app.route('/register', methods=['POST'])
def register():
    success = True

    if len(request.form['name']) < 2:
        success = False
        flash("Name must be longer than 2")

    if not EMAIL_REGEX.match(request.form['email']):
        success = False
        flash("Invalid email")

    if len(request.form['password1']) < 8:
        success = False
        flash("Password must be longer than 8")

    if request.form['password1'] != request.form['password2']:
        success = False
        flash("Password confirmation does not match")

    if success:
        User.add_user(request.form)
        session['user'] = request.form['email']
        return redirect('/success')
    
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    success = True

    if not EMAIL_REGEX.match(request.form['email']):
        success = False
        flash("Invalid email")

    if len(request.form['password1']) < 8:
        success = False
        flash("Password must be longer than 8")

    if User.get_user(request.form) == None:
        success = False
        flash("Invalid email/password")

    if success:
        session['user'] = request.form['email']
        return redirect('/success')
    
    return redirect('/')


@app.route('/success')
def success():
    if session.get('user') == None:
        return redirect('/')

    return render_template('success.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

