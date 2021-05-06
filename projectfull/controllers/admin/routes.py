from app import app
from flask import request, redirect, render_template
from model import db, Slider, About, Profession, Skill, Info, Employer, Project, Project_image
from flask_sqlalchemy import SQLAlchemy
import os

@app.route("/admin")
def admin():
    employers = Employer.query.all()
    slides = Slider.query.all()
    about = About.query.first()
    infoList = Info.query.all()
    professions = Profession.query.all()
    skills = Skill.query.all()
    return render_template("admin/index/index.html", slides = slides, about = about, professions = professions, skills = skills, infoList = infoList, employers = employers)


# Slider
@app.route("/admin/addslide", methods = ["GET", "POST"])
def addslide():
    if request.method == "POST":
        image = request.files["img"]
        image_name = image.filename
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))

        db.session.add(Slider(
            image = image_name
        ))
        db.session.commit()
        return redirect("/admin/addslide")
    return render_template("admin/index/slider/addslide.html")

@app.route("/admin/updateslide/<id>", methods = ["GET", "POST"])
def updateslide(id):
    slide = Slider.query.get(int(id))
    if request.method == "POST":
        slide.image = request.files["img"].filename
        db.session.commit()
        return redirect("/admin")
    return render_template("admin/index/slider/updateslide.html", slide = slide)

@app.route("/admin/deleteslide/<id>")
def deleteslide(id):
    db.session.delete(Slider.query.get(int(id)))
    db.session.commit()
    return redirect("/admin")
    

# About
@app.route("/admin/updateabout", methods = ["GET", "POST"])
def updateabout():
    about = About.query.get(1)
    if request.method == "POST":
        about.title = request.form["title"]
        about.content = request.form["content"]
        db.session.commit()
        return redirect("/admin")
    return render_template("admin/index/homeAbout/about.html", about = about)


# Info
@app.route("/admin/addinfo", methods = ["GET", "POST"])
def addinfo():
    if request.method == "POST":
        db.session.add(Info(name = request.form["name"], value = int(request.form["value"])))
        db.session.commit()
        return redirect("/admin/addinfo")
    return render_template("admin/index/info/addinfo.html")

@app.route("/admin/updateinfo/<id>", methods = ["GET", "POST"])
def updateinfo(id):
    info = Info.query.get(int(id))
    if request.method == "POST":
        info.name = request.form["name"]
        info.value = int(request.form["value"])
        db.session.commit()
        return redirect("/admin")
    return render_template("admin/index/info/updateinfo.html", info = info)

@app.route("/admin/deleteinfo/<id>")
def deleteinfo(id):
    db.session.delete(Info.query.get(int(id)))
    db.session.commit()
    return redirect("/admin")


# Employer
@app.route("/admin/addemployer", methods = ["GET", "POST"])
def addemployer():
    if request.method == "POST":
        image = request.files["img"]
        image_name = image.filename
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))

        db.session.add(Employer(
            fullname = request.form["fullname"],
            profession = request.form["profession"],
            photo = image_name
        ))
        db.session.commit()
        return redirect("/admin/addemployer")
    return render_template("admin/index/employers/addemployer.html")

@app.route("/admin/updateemployer/<id>", methods = ["GET", "POST"])
def updateemployer(id):
    employer = Employer.query.get(int(id))
    if request.method == "POST":
        employer.fullname = request.form["fullname"]
        employer.profession = request.form["profession"]
        image = request.files["img"]
        image_name = image.filename
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))
        employer.photo = image_name
        db.session.commit()
        return redirect("/admin")
    return render_template("admin/index/employers/updateemployer.html", employer = employer)

@app.route("/admin/deleteemployer/<id>")
def deleteemployer(id):
    db.session.delete(Employer.query.get(int(id)))
    db.session.commit()
    return redirect("/admin")


# Professions
@app.route("/admin/addprofession", methods = ["GET", "POST"])
def addprofession():
    if request.method == "POST":
        image = request.files["img"]
        image_name = image.filename
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))

        db.session.add(Profession(
            name = request.form["profession_name"],
            description = request.form["short_desc"],
            image = image_name
        ))
        db.session.commit()
        return redirect("/admin/addprofession")
    return render_template("admin/index/professions/addprofession.html")

@app.route("/admin/updateprofession/<id>", methods = ["GET", "POST"])
def updateprofession(id):
    profession = Profession.query.get(int(id))
    if request.method == "POST":
        profession.name = request.form["profession_name"]
        profession.description = request.form["short_desc"]
        image = request.files["img"]
        image_name = image.filename
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))
        profession.image = image_name
        db.session.commit()
        return redirect("/admin")
    return render_template("admin/index/professions/updateprofession.html", profession = profession)

@app.route("/admin/deleteprofession/<id>")
def deleteprofession(id):
    db.session.delete(Profession.query.get(int(id)))
    db.session.commit()
    return redirect("/admin")


# Skills
@app.route("/admin/addskill", methods = ["GET", "POST"])
def addskill():
    professions = Profession.query.all()
    if request.method == "POST":
        db.session.add(Skill(name = request.form["skill"], profession_id = int(request.form["profession"])))
        db.session.commit()
        return redirect("/admin/addskill")
    return render_template("admin/index/skills/addskill.html", professions = professions)

@app.route("/admin/updateskill/<id>", methods = ["GET", "POST"])
def updateskill(id):
    professions = Profession.query.all()
    skill = Skill.query.get(int(id))
    if request.method == "POST":
        skill.name = request.form["skill"]
        skill.profession_id = request.form["profession"]
        db.session.commit()
        return redirect("/admin")
    return render_template("admin/index/skills/updateskill.html", professions = professions, skill = skill)

@app.route("/admin/deleteskill/<id>")
def deleteskill(id):
    db.session.delete(Skill.query.get(int(id)))
    db.session.commit()
    return redirect("/admin")