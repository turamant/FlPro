

from flask import render_template, flash, request

from app import app, db
from forms import NamerForm, UserForm
from models import Users


@app.route('/user/add', methods=['POST', 'GET'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data,
                         email=form.email.data,
                         favorite_color=form.favorite_color.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        form.favorite_color.data = ''
        flash("User Added Successed!")
    our_users = Users.query.order_by(Users.date_added)
    return render_template('add_user.html',
                           form=form,
                           name=name,
                           our_users=our_users)

# loalhost:8000
@app.route('/')
def index():
    secret = "<h1>{}</h1>".format(app.config['SECRET_KEY'])
    pizza_list = ["pepperony", "margarita", "napoly", "for season"]
    flash("Welcome To Our Website!")
    return render_template('index.html', data=secret, pizza_list=pizza_list)

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

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfull")
    return render_template('name.html',
                           name=name,
                           form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = UserForm()
    name_to_update = Users.query.get_or_404(id)
    if request.method == 'POST':
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        name_to_update.favorite_color = request.form['favorite_color']
        try:
            db.session.commit()
            flash('User update successfull!')
            return render_template('update.html',
                                   form=form,
                                   name_to_update=name_to_update
                                   )
        except:
            flash('Errror User update ...try again!')
            return render_template('update.html',
                                   form=form,
                                   name_to_update=name_to_update
                                   )
    else:
        return render_template('update.html',
                               form=form,
                               name_to_update=name_to_update
                               )
