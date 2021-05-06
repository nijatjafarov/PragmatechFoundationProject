from app import app
from flask import request, redirect, render_template
from model import db, Slider, About, Info, Employer, Profession, Skill, Project, Project_image
from flask_sqlalchemy import SQLAlchemy

@app.route("/")
def index():
    employers = Employer.query.all()
    slides = Slider.query.all()
    about = About.query.first()
    infoList = Info.query.all()
    professions = Profession.query.all()
    skills = Skill.query.all()
    return render_template("app/index.html", slides = slides, about = about, infoList = infoList, employers = employers, professions = professions, skills = skills)