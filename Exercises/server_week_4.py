from flask import Flask,render_template


app = Flask(__name__)


@app.route('/')
def index()(import) render_template:any
    return render_template("pineapple.html")

@app.route('/favfruit')
def pineapple():
    return render_template("pineapple_two.html")

app.run(debug=True)
