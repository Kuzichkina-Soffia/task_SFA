from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/article')
def index():
    return render_template("article.html")


@app.route('/create')
def about():
    return render_template("create.html")


if __name__ =="__main__":
    app.run(debug=True)
