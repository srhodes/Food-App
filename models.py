from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Food(db.Model):
    __tablename__ = 'food'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(50),
                    nullable=False,
                    unique=True)
    carbohydrades = db.Column(db.Float, nullable=False, default=13.81)
    proteins = db.Column(db.Float, nullable=False, default=0.26)            
    fats = db.Column(db.Float, nullable=False, default=0.17)            
    calorie = db.Column(db.Integer, nullable=False, default=52)            
    weight = db.Column(db.Integer, nullable=False, default=100)

class Carbs(db.Model):
    __tablename__ = 'carbs'

    foodId = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    carbohydrades = db.Column(db.Float, nullable=False, default=13.81)
    fructose = db.Column(db.Float, nullable=False, default=13.81)
    sucrose = db.Column(db.Float, nullable=False, default=13.81)
    lactose = db.Column(db.Float, nullable=False, default=13.81)
    glucose = db.Column(db.Float, nullable=False, default=13.81)
    fiber = db.Column(db.Float, nullable=False, default=13.81)


class Lipids(db.Model):
    __tablename__ = 'lipids'

    foodId = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    fat = db.Column(db.Float, nullable=False, default=13.81)
    saturated = db.Column(db.Float, nullable=False, default=13.81)
    mono = db.Column(db.Float, nullable=False, default=13.81)
    poly = db.Column(db.Float, nullable=False, default=13.81)
    dha = db.Column(db.Float, nullable=False, default=13.81)
    transFat = db.Column(db.Float, nullable=False, default=13.81)

class Proteins(db.Model):
    __tablename__ = 'proteins'

    foodId = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    protein = db.Column(db.Float, nullable=False, default=13.81)
    arginine = db.Column(db.Float, nullable=False, default=13.81)
    cystine = db.Column(db.Float, nullable=False, default=13.81)
    glutamicAcid = db.Column(db.Float, nullable=False, default=13.81)
  