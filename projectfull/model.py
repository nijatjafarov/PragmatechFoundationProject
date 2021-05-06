from flask_sqlalchemy import SQLAlchemy
from app import app
import datetime

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
UPLOAD_FOLDER='static/app/uploads/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

db = SQLAlchemy(app)

class Slider(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(100), unique = True, nullable = False)

class About(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30), unique = True, nullable = False)
    content = db.Column(db.Text, unique = True, nullable = False)

class Info(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = True, nullable = False)
    value = db.Column(db.Integer, nullable = False)

class Employer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(50), unique = True, nullable = False)
    profession = db.Column(db.String(40), nullable = False)
    photo = db.Column(db.String(100), unique = True, nullable = False)

class Profession(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = True, nullable = False)
    description = db.Column(db.String(120), unique = True)
    image = db.Column(db.String(100), unique = True, nullable = False)
    skills = db.relationship("Skill", backref = "profession", lazy = True)
    projects = db.relationship("Project", backref = "profession", lazy = True)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(70), nullable = False)
    profession_id = db.Column(db.Integer, db.ForeignKey('profession.id'), nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, nullable = False)
    content = db.Column(db.Text)
    cover_image = db.Column(db.String(100), unique = True, nullable = False)
    date = db.Column(db.DateTime, nullable = False)
    profession_id = db.Column(db.Integer, db.ForeignKey("profession.id"))
    images = db.relationship("Project_image", backref = "project", lazy = True)

class Project_image(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(100), unique = True, nullable = False)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), default = datetime.date.today())
