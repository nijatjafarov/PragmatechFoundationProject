from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

class Slider(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(100), unique = True, nullable = False)

class About(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30), nullable = False)
    content = db.Column(db.Text, nullable = False)

class Info(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = True, nullable = False)
    value = db.Column(db.Integer, nullable = False)

class Employer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(50), nullable = False)
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
    show_on_home = db.Column(db.Boolean)
    profession_id = db.Column(db.Integer, db.ForeignKey("profession.id"))
    images = db.relationship("Project_image", backref = "project", lazy = True)

class Project_image(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(100), unique = True, nullable = False)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))

class About_page(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(100), nullable = False)
    title = db.Column(db.String(80), nullable = False)
    content = db.Column(db.Text, nullable = False)

class Contact_page(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title1 = db.Column(db.String(80))
    title2 = db.Column(db.String(80))
    image = db.Column(db.String(100))

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = True, nullable = False)
    value = db.Column(db.String(30), unique = True, nullable = False)
    show_on_footer = db.Column(db.Boolean)
    show_on_contact = db.Column(db.Boolean)

class User_message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(80), nullable = False)
    message = db.Column(db.Text, nullable = False)
    date = db.Column(db.DateTime, nullable = False)

class Social_media(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    icon_url = db.Column(db.String(80))
    link = db.Column(db.String(120), nullable = False)
    show_on_home = db.Column(db.Boolean)
    show_on_footer = db.Column(db.Boolean)
    show_on_project = db.Column(db.Boolean)
    show_on_about = db.Column(db.Boolean)

