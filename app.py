from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
# from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField
from wtforms.validators import InputRequired, Length, ValidationError
from models import db, connect_db, User
from secrets import API_SECRET_KEY
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///food_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "mysecret123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
debug = DebugToolbarExtension(app)

connect_db(app)

class loginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

class AddFoodInfo(FlaskForm):
    name = StringField("Food Name")
    calories = FloatField("Calories")
    carbs = FloatField("carbs")
    fat = FloatField("fat")
    protein = FloatField("protein")

@app.route('/home')
def index():
    # Document at https://spoonacular.com/food-api/docs#Get-Recipe-Information

    res = requests.get('https://api.spoonacular.com/recipes/716429/information?apiKey=d7c35df411774b8abdc4c5197ab01533')
    # https://api.spoonacular.com/recipes/716429/information?apiKey=d7c35df411774b8abdc4c5197ab01533&includeNutrition=true
    # POST Request - https://spoonacular.com/food-api/docs#Create-Recipe-Card
    # GET Request - https://spoonacular.com/food-api/docs#Get-Recipe-Card

    # https://api.spoonacular.com/mealplanner/generate?timeFrame=day,targetCalories=2000&apiKey=d7c35df411774b8abdc4c5197ab01533 

    # res = requests.get('https://api.spoonacular.com/recipes/716429/information', params={'apiKey': API_SECRET_KEY, 'includeNutrition': True})
    
    res = requests.get('https://api.spoonacular.com/mealplanner/generate', params={'apiKey': API_SECRET_KEY, 'timeFrame':'day', 'targetCalories': 2000})


    data = res.json()
    # img = data['image']

    # obj = {'img': img}
    firstMealID= data['meals'][0]['id']
    secondMealID = data['meals'][1]['id']
    thirdMealID = data['meals'][2]['id']
    mealList = [firstMealID, secondMealID, thirdMealID]

    # for meal in mealList
    # print(meal)
    #
    
    
    res1 = requests.get(f'https://api.spoonacular.com/recipes/{firstMealID}/information', params={'apiKey': API_SECRET_KEY, 'includeNutrition': True})
    res2 = requests.get(f'https://api.spoonacular.com/recipes/{secondMealID}/information', params={'apiKey': API_SECRET_KEY, 'includeNutrition': True})
    res3 = requests.get(f'https://api.spoonacular.com/recipes/{thirdMealID}/information', params={'apiKey': API_SECRET_KEY, 'includeNutrition': True})

    data1 = res1.json() 
    data2 = res2.json() 
    data3 = res3.json() 
    resList = [data1['image'], data2['image'], data3['image']]

    # for meal in mealList:
    #     print(meal)
    #     resList.append(meal) 
    #     print(resList)

    # data2 = res2.json()
    return render_template("index.html", name1 = data1['image'], name2 =data2['image'] , name3=data3['image'])

@app.route('/price')
def price():
    # Document at https://spoonacular.com/food-api/docs#Get-Recipe-Information

    res = requests.get('https://api.spoonacular.com/recipes/716429/information?apiKey=d7c35df411774b8abdc4c5197ab01533')
    # https://api.spoonacular.com/recipes/716429/information?apiKey=d7c35df411774b8abdc4c5197ab01533&includeNutrition=true
    # POST Request - https://spoonacular.com/food-api/docs#Create-Recipe-Card
    # GET Request - https://spoonacular.com/food-api/docs#Get-Recipe-Card

    # https://api.spoonacular.com/mealplanner/generate?timeFrame=day,targetCalories=2000&apiKey=d7c35df411774b8abdc4c5197ab01533 

    # res = requests.get('https://api.spoonacular.com/recipes/716429/information', params={'apiKey': API_SECRET_KEY, 'includeNutrition': True})
    
    res = requests.get('https://api.spoonacular.com/mealplanner/generate', params={'apiKey': API_SECRET_KEY, 'timeFrame':'day', 'targetCalories': 2000})


    data = res.json()
    # img = data['image']

    # obj = {'img': img}
    firstMealID= data['meals'][0]['id']
    secondMealID = data['meals'][1]['id']
    thirdMealID = data['meals'][2]['id']
    mealList = [firstMealID, secondMealID, thirdMealID]

    # for meal in mealList
    # print(meal)
    #
    
    
    res1 = requests.get(f'https://api.spoonacular.com/recipes/{firstMealID}/information', params={'apiKey': API_SECRET_KEY, 'includeNutrition': True})
    res2 = requests.get(f'https://api.spoonacular.com/recipes/{secondMealID}/information', params={'apiKey': API_SECRET_KEY, 'includeNutrition': True})
    res3 = requests.get(f'https://api.spoonacular.com/recipes/{thirdMealID}/information', params={'apiKey': API_SECRET_KEY, 'includeNutrition': True})

    data1 = res1.json() 
    data2 = res2.json() 
    data3 = res3.json() 
    resList = [data1['image'], data2['image'], data3['image']]


    # for meal in mealList:
    #     print(meal)
    #     resList.append(meal) 
    #     print(resList)

    # data2 = res2.json()
    return render_template("price.html", 
    name1 = data1['image'], 
    name2 = data2['image'] , 
    name3 = data3['image'], 
    diet1 = data1['diets'],
    diet2 = data2['diets'],
    diet3 = data3['diets'],
    inst1 = data1['instructions'],
    inst2 = data2['instructions'],
    inst3 = data3['instructions']
    )

@app.route('/nutrients', methods=["GET", "POST"])
def nutrients():
    # Document at https://spoonacular.com/food-api/docs#Get-Recipe-Information

    # res = requests.get('https://api.spoonacular.com/recipes/findByNutrients?minCarbs=10&maxCarbs=50&number=2&apiKey=d7c35df411774b8abdc4c5197ab01533')
    # https://api.spoonacular.com/recipes/716429/information?apiKey=d7c35df411774b8abdc4c5197ab01533&includeNutrition=true
    # POST Request - https://spoonacular.com/food-api/docs#Create-Recipe-Card
    # GET Request - https://spoonacular.com/food-api/docs#Get-Recipe-Card

    # https://api.spoonacular.com/mealplanner/generate?timeFrame=day,targetCalories=2000&apiKey=d7c35df411774b8abdc4c5197ab01533 

    # res = requests.get('https://api.spoonacular.com/recipes/716429/information', params={'apiKey': API_SECRET_KEY, 'includeNutrition': True})
    
    form = AddFoodInfo()
    res = requests.get('https://api.spoonacular.com/recipes/findByNutrients', params={'apiKey': API_SECRET_KEY, 'minCarbs':10, 'maxCarbs': 50, 'number': 2})


    data = res.json()
    # img = data['image']

    # obj = {'img': img}
    firstMealID= data[0]['id']
    firstMealCalories = data[0]['calories']
    firstMealProtein = data[0]['protein']
    firstMealFat = data[0]['fat']

    secondMealID = data[1]['id']
    secondMealCalories = data[1]['calories']
    secondMealProtein = data[1]['protein']
    secondMealFat = data[1]['fat']

    
    mealList = [firstMealID, secondMealID]

    # for meal in mealList
    # print(meal)
    #
    
    
    res1 = requests.get(f'https://api.spoonacular.com/recipes/{firstMealID}/information', params={'apiKey': API_SECRET_KEY, 'includeNutrition': True})
    res2 = requests.get(f'https://api.spoonacular.com/recipes/{secondMealID}/information', params={'apiKey': API_SECRET_KEY, 'includeNutrition': True})


    data1 = res1.json() 
    data2 = res2.json() 

    resList = [data1['image'], data2['image']]


    # for meal in mealList:
    #     print(meal)
    #     resList.append(meal) 
    #     print(resList)

    # data2 = res2.json()
    if form.validate_on_submit():
        name = form.name.data
        calories = form.calories.data
        carbs = form.calories.data
        fat = form.fat.data
        protein = form.protein.data

        if name == firstMealTitle:
            return render_template("nutrients.html",
            firstMealImage = data1['image'],
            firstMealTitle = data[0]['title'],
            secondMealTitle = data[1]['title'], 
            secondMealImage = data2['image'], 
            firstMealCalories = data[0]['calories'],
            firstMealProtein = data[0]['protein'],
            firstMealFat = data[0]['fat'],
            firstMealCarbs = data[0]['carbs'],
            secondMealCalories = data[1]['calories'],
            secondMealProtein = data[1]['protein'],
            secondMealFat = data[1]['fat'],
            secondMealCarbs = data[1]['carbs'],
            form=form
            )

        if calories == firstMealCalories or calories == secondMealCalories:
            return render_template("nutrients.html", 
             firstMealImage = data1['image'],
             firstMealTitle = data[0]['title'],
             firstMealCalories = data[0]['calories'],
             secondMealTitle = data[1]['title'], 
             secondMealImage = data2['image'],
             secondMealCalories = data[1]['calories'],
             form=form 
             )
        if carbs == firstMealCarbs or carbs == secondMealCarbs:
            return render_template("nutrients.html", 
             firstMealImage = data1['image'],
             firstMealTitle = data[0]['title'],
             firstMealCarbs = data[0]['carbs'],
             secondMealTitle = data[1]['title'], 
             secondMealImage = data2['image'],
             secondMealCarbs = data[1]['carbs'],
             form=form 
             )
        if fat == firstMealFat or fat == secondMealFat:
            return render_template("nutrients.html", 
             firstMealImage = data1['image'],
             firstMealTitle = data[0]['title'],
             firstMealFat = data[0]['fat'],
             secondMealTitle = data[1]['title'], 
             secondMealImage = data2['image'],
             secondMealFat = data[1]['fat'],
             form=form 
             )
        if protein == firstMealProtein or protein == secondMealProtein:
            return render_template("nutrients.html", 
             firstMealImage = data1['image'],
             firstMealTitle = data[0]['title'],
             firstMealProtein = data[0]['protein'],
             secondMealTitle = data[1]['title'], 
             secondMealImage = data2['image'],
             secondMealProtein = data[1]['protein'],
             form=form 
             )
        else:
            redirect("nutritents.html")

    return render_template("nutrients.html", 
    # firstMealImage = data1['image'],
    # firstMealTitle = data[0]['title'],
    # secondMealTitle = data[1]['title'], 
    # secondMealImage = data2['image'], 
    # firstMealCalories = data[0]['calories'],
    # firstMealProtein = data[0]['protein'],
    # firstMealFat = data[0]['fat'],
    # firstMealCarbs = data[0]['carbs'],
    # secondMealCalories = data[1]['calories'],
    # secondMealProtein = data[1]['protein'],
    # secondMealFat = data[1]['fat'],
    # secondMealCarbs = data[1]['carbs'],
    form=form
    )

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
