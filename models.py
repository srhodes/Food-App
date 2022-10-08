from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    @classmethod
    def register(cls, username, pwd):
        hashed = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hashed.decode("utf8")

        return cls(username=username, password=hashed_utf8)
    
    @classmethod
    def authenticate(cls, username, pwd):

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            return u
        else:
            return False
        

class Food(db.Model):
    __tablename__ = 'food'

    foodId = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(50),
                    nullable=False,
                    unique=True)
    carbohydrates = db.Column(db.Float, nullable=False, default=13.81)
    proteins = db.Column(db.Float, nullable=False, default=0.26)            
    fats = db.Column(db.Float, nullable=False, default=0.17)            
    calorie = db.Column(db.Integer, nullable=False, default=52)            
    weight = db.Column(db.Integer, nullable=False, default=100)

class Carbs(db.Model):
    __tablename__ = 'carbs'

    carbsId = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    foodId = db.Column(db.Integer, 
                     db.ForeignKey('food.foodId'),
                     nullable=False)
    carbohydrates = db.Column(db.Float, nullable=False, default=13.81)
    fructose = db.Column(db.Float, nullable=False, default=13.81)
    sucrose = db.Column(db.Float, nullable=False, default=13.81)
    lactose = db.Column(db.Float, nullable=False, default=13.81)
    glucose = db.Column(db.Float, nullable=False, default=13.81)
    fiber = db.Column(db.Float, nullable=False, default=13.81)


class Lipids(db.Model):
    __tablename__ = 'lipids'

    lipidsId = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    foodId = db.Column(db.Integer, 
                     db.ForeignKey('food.foodId'),
                     nullable=False)
    fat = db.Column(db.Float, nullable=False, default=13.81)
    saturated = db.Column(db.Float, nullable=False, default=13.81)
    mono = db.Column(db.Float, nullable=False, default=13.81)
    poly = db.Column(db.Float, nullable=False, default=13.81)
    dha = db.Column(db.Float, nullable=False, default=13.81)
    transFat = db.Column(db.Float, nullable=False, default=13.81)

class Proteins(db.Model):
    __tablename__ = 'proteins'

    proteinsId = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    foodId = db.Column(db.Integer, 
                     db.ForeignKey('food.foodId'),
                     nullable=False)
    protein = db.Column(db.Float, nullable=False, default=13.81)
    arginine = db.Column(db.Float, nullable=False, default=13.81)
    cystine = db.Column(db.Float, nullable=False, default=13.81)
    glutamicAcid = db.Column(db.Float, nullable=False, default=13.81)
  