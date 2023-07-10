from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "my super secret Counter key!"

@app.route('/')
def root():
    # Create the key if it doesn't exist
    if (session.get('counter') == None):
        session['counter'] = 0
    
    session['counter'] += 1
    return render_template("counter.html")

@app.route('/add_two')
def add_two():
    # This route will +1 and then root will do another +1
    session['counter'] += 1
    return redirect('/')

@app.route('/manual_increment', methods=['POST'])
def manual_increment():
    # Make sure the input isn't empty
    # You'd also want to make sure that it's an actual int() parsable 
    # string and not letters but I'm not sure how to do that here
    if (request.form.get('manual_increment') != ''):
        # -1 because of the root's +1
        session['counter'] += int(request.form.get('manual_increment')) - 1 
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
