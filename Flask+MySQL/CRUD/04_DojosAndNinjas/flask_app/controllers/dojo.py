
from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def root():
    return render_template("all_dojos.html", all_dojos=Dojo.get_all())

@app.route('/dojos/<int:dojo_id>')
def single_dojo(dojo_id):
    return render_template("single_dojo.html", dojo=Dojo.get_one(dojo_id))

@app.route('/submit_dojo', methods=['POST'])
def submit_dojo():
    Dojo.add_dojo(request.form)
    return redirect('/')
