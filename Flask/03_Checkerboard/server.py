from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def board_default():
    return render_template("checkerboard.html", width=8, height=8)

@app.route('/<int:height>')
def board_dynamic_height(height):
    return render_template("checkerboard.html", width=8, height=height)

@app.route('/<int:width>/<int:height>')
def board_dynamic(width, height):
    return render_template("checkerboard.html", width=width, height=height)

if __name__=="__main__":
    app.run(debug=True)
