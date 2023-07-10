from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return f"Hi {name}!"

@app.route('/repeat/<amount>/<string>')
def repeat(amount, string):
    amount = int(amount)
    print_string = ""
    for i in range(amount):
        print_string += string + "\n"
    return print_string

if __name__=="__main__":
    app.run(debug=True)
