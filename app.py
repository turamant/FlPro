from flask import Flask, render_template

app = Flask(__name__)


# loalhost:8000
@app.route('/')
def index():
    name = "Python Flask"
    pizza_list = ["pepperony", "margarita", "napoly", "for season"]
    return render_template('index.html', data=name, pizza_list=pizza_list)

# localhost:8000/user/name
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user=name)


# invalid Custom Error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__=='__main__':
    app.run(debug=True, port=8000)

