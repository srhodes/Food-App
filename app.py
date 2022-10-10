from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
# from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from models import db, connect_db, User
from secrets import API_SECRET_KEY
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///food_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "mysecret123"
debug = DebugToolbarExtension(app)

connect_db(app)

class loginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")


@app.route('/home')
def index():
    # Document at https://spoonacular.com/food-api/docs#Get-Recipe-Information

    # res = requests.get('https://api.spoonacular.com/recipes/716429/information?apiKey=d7c35df411774b8abdc4c5197ab01533')
    
    # res = requests.get('https://api.spoonacular.com/recipes/716429/information?apiKey=d7c35df411774b8abdc4c5197ab01533')
    res = requests.get('https://api.spoonacular.com/recipes/716429/information', params={'apiKey': API_SECRET_KEY})
  
    data = res.json()
    img = data['image']

    obj = {'img': img}
    return render_template("index.html", name = img)

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = loginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        new_user = User.register(username, password)
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.id
        flash('Welcome! Successfully Created Your Account! ')
        return redirect('/user')
    
    return render_template('register.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():  
    form = loginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.authenticate(username, password)
        if user:
            session["user_id"] = user.id
            return redirect('/user')
        else:
            form.username.errors = ['Invalid username/password.']

    return render_template("login.html", form=form)

@app.route('/user')
def user():
    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/home")

    else:
        return render_template("user.html")

@app.route('/logout')
def logout():
    session.pop("user_id")
    return redirect("/home")

@app.route('/diet')
def diet():  
    return render_template("diet.html")


# try:
#     session.commit()
# except:
#     session.rollback()
#     raise
# finally:
#     session.close()
