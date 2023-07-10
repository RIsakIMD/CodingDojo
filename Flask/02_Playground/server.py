from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return "Welcome To Playground!"

@app.route('/play')
def play_default():
    return render_template("play.html", box_count=3)


@app.route('/play/<int:box_count>')
def play_dynamic(box_count):
    return render_template("play.html", box_count=box_count, custom_color="lightskyblue")

@app.route('/play/<int:box_count>/<custom_color>')
def play_dynamic_colored(box_count, custom_color):
    return render_template("play.html", box_count=box_count, custom_color=custom_color)

if __name__=="__main__":
    app.run(debug=True)
