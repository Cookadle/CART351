from flask import Flask,render_template


app = Flask(__name__)


@app.route('/favfruit')
def pineapple():
    return render_template("pineapple.html")

@app.route('/three/<name>')
def three(name):
    return render_template("pineapple_three.html,someNewVar =name")



app.run(debug=True)