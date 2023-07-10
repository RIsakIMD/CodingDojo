
from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "my super secret key!"

@app.route('/')
def root():
    session.clear()
    return render_template("survey.html")

@app.route('/submit', methods=['POST'])
def submit():
    for key in request.form:
        session[key] = request.form[key]
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)
