import random
from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "my super secret key!"

@app.route('/')
def root():
    if (session.get('magic_number') == None):
        session['magic_number'] = random.randint(1, 100)
        session['guess'] = -1

    print(f"you guessed {session['guess']} {session['magic_number']}")
    return render_template("game.html")

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    session['guess'] = request.form.get('submit_guess')
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
