
from flask import render_template, request, redirect
from flask_app import app
from flask_app.models import ninja, dojo

@app.route('/create_ninja')
def create_ninja():
    return render_template("create_ninja.html", all_dojos=dojo.Dojo.get_all())

@app.route('/submit_ninja', methods=['POST'])
def submit_ninja():
    ninja.Ninja.add_ninja(request.form)
    print(request.form)
    return redirect('/dojos/' + request.form['dojo_id'])
