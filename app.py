from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
# from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from models import db, connect_db, User
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
    res = requests.get('https://api.spoonacular.com/recipes/69095/information?apiKey=d7c35df411774b8abdc4c5197ab01533')
    return render_template("index.html", name = res.text)

# @app.route('/register')
# def register():

@app.route('/login', methods=["GET", "POST"])
def login():  
    form = loginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.authenticate(username, password)
        if user:
            return redirect('/home')
        else:
            form.username.errors = ['Invalid username/password.']

    return render_template("login.html", form=form)

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
