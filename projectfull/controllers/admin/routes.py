from re import template
from app import app
from flask import request, redirect, render_template, url_for
from model import db, Slider, About, Profession, Skill,\
    Info, Employer, Project, Project_image, About_page,\
    Contact_page, Contact, User_message, Social_media
from form import SliderForm, AboutForm, InfoForm, EmployerForm,\
    ProfessionForm, SkillForm, ProjectForm, ProjectImageForm,\
    AboutPageForm, ContactPageForm, ContactForm, SocialMediaForm
from werkzeug.utils import secure_filename
import os
import datetime

def checkLogin(parameter):
    loginStat = request.cookies.get("loginStatus")
    if loginStat == "True":
        return parameter
    else:
        return redirect(url_for("login"))

# @login_required
@app.route("/admin")
def admin():
    employers = Employer.query.all()
    slides = Slider.query.all()
    about = About.query.first()
    infoList = Info.query.all()
    professions = Profession.query.all()
    skills = Skill.query.all()
    template = render_template("admin/index/index.html", 
    slides = slides, about = about, Profession = Profession, 
    professions = professions, skills = skills, infoList = infoList,
    employers = employers)
    return checkLogin(template)


# Slider
@app.route("/admin/addslide", methods = ["GET", "POST"])
def addslide():
    form = SliderForm()
    if form.validate_on_submit():
        image = form.img.data
        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))

        db.session.add(Slider(
            image = image_name
        ))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/index/slider/addslide.html", form = form)
    return checkLogin(template)

@app.route("/admin/updateslide/<id>", methods = ["GET", "POST"])
def updateslide(id):
    slide = Slider.query.get(int(id))
    form = SliderForm()
    if form.validate_on_submit():
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], slide.image)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], slide.image))
        img = form.img.data
        slide.image = secure_filename(img.filename)
        img.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(img.filename)))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/index/slider/updateslide.html", form = form)
    return checkLogin(template)

@app.route("/admin/deleteslide/<id>")
def deleteslide(id):
    db.session.delete(Slider.query.get(int(id)))
    db.session.commit()
    template = redirect("/admin")
    return checkLogin(template)

# About
@app.route("/admin/updateabout", methods = ["GET", "POST"])
def updateabout():
    about = About.query.get(1)
    form = AboutForm()
    if form.validate_on_submit():
        about.title = form.title.data
        about.content = form.content.data
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/index/homeAbout/about.html", about = about, form = form)
    return checkLogin(template)


# Info
@app.route("/admin/addinfo", methods = ["GET", "POST"])
def addinfo():
    form = InfoForm()
    if form.validate_on_submit():
        db.session.add(Info(name = form.name.data, value = int(form.value.data)))
        db.session.commit()
        return redirect(url_for("addinfo"))
    template = render_template("admin/index/info/addinfo.html", form = form)
    return checkLogin(template)

@app.route("/admin/updateinfo/<id>", methods = ["GET", "POST"])
def updateinfo(id):
    info = Info.query.get(int(id))
    form = InfoForm()
    if form.validate_on_submit():
        info.name = form.name.data
        info.value = int(form.value.data)
        db.session.commit()
        return redirect("/admin")
    template = render_template("admin/index/info/updateinfo.html", info = info, form = form)
    return checkLogin(template)

@app.route("/admin/deleteinfo/<id>")
def deleteinfo(id):
    db.session.delete(Info.query.get(int(id)))
    db.session.commit()
    template = redirect("/admin")
    return checkLogin(template)


# Employer
@app.route("/admin/addemployer", methods = ["GET", "POST"])
def addemployer():
    form = EmployerForm()
    if form.validate_on_submit():
        image = form.img.data
        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))
        db.session.add(Employer(
            fullname = form.fullname.data,
            profession = form.profession.data,
            photo = image_name
        ))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/index/employers/addemployer.html", form = form)
    return checkLogin(template)

@app.route("/admin/updateemployer/<id>", methods = ["GET", "POST"])
def updateemployer(id):
    employer = Employer.query.get(int(id))
    form = EmployerForm()
    if form.validate_on_submit():
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], employer.photo)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], employer.photo))
        employer.fullname = form.fullname.data
        employer.profession = form.profession.data
        image = form.img.data
        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))
        employer.photo = image_name
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/index/employers/updateemployer.html", employer = employer, form = form)
    return checkLogin(template)

@app.route("/admin/deleteemployer/<id>")
def deleteemployer(id):
    db.session.delete(Employer.query.get(int(id)))
    db.session.commit()
    template = redirect("/admin")
    return checkLogin(template)


# Professions
@app.route("/admin/addprofession", methods = ["GET", "POST"])
def addprofession():
    form = ProfessionForm()
    if form.validate_on_submit():
        image = form.img.data
        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))

        db.session.add(Profession(
            name = form.name.data,
            description = form.description.data,
            image = image_name
        ))
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/index/professions/addprofession.html", form = form)
    return checkLogin(template)

@app.route("/admin/updateprofession/<id>", methods = ["GET", "POST"])
def updateprofession(id):
    profession = Profession.query.get(int(id))
    form = ProfessionForm()
    if form.validate_on_submit():
        profession.name = form.name.data
        profession.description = form.description.data
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], profession.image)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], profession.image))
        image = form.img.data
        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))
        profession.image = image_name
        db.session.commit()
        return redirect(url_for("admin"))
    template = render_template("admin/index/professions/updateprofession.html", profession = profession, form = form)
    return checkLogin(template)

@app.route("/admin/deleteprofession/<id>")
def deleteprofession(id):
    db.session.delete(Profession.query.get(int(id)))
    db.session.commit()
    template = redirect(url_for("admin"))
    return checkLogin(template)


# Skills
@app.route("/admin/addskill", methods = ["GET", "POST"])
def addskill():
    professions = Profession.query.all()
    form = SkillForm()
    if form.validate_on_submit():
        db.session.add(Skill(name = form.skill.data, profession_id = request.form["profession"]))
        db.session.commit()
        return redirect(url_for("addskill"))
    template =  render_template("admin/index/skills/addskill.html", professions = professions, form = form)
    return checkLogin(template)

@app.route("/admin/updateskill/<id>", methods = ["GET", "POST"])
def updateskill(id):
    professions = Profession.query.all()
    skill = Skill.query.get(int(id))
    selected_profession = Profession.query.get(skill.profession_id)
    form = SkillForm()
    if request.method == "POST":
        skill.name = form.skill.data
        skill.profession_id = request.form["profession"]
        db.session.commit()
        return redirect("/admin")
    template = render_template("admin/index/skills/updateskill.html", professions = professions, skill = skill, selected_profession = selected_profession, form = form)
    return checkLogin(template)

@app.route("/admin/deleteskill/<id>")
def deleteskill(id):
    db.session.delete(Skill.query.get(int(id)))
    db.session.commit()
    template = redirect("/admin")
    return checkLogin(template)




# Portfolio page
@app.route("/admin/portfolio")
def portfolio():
    project_images = Project_image.query.all()
    template = render_template("admin/portfolio/portfolio.html", Project = Project, project_images = project_images, Profession = Profession)
    return checkLogin(template)

# Project
@app.route("/admin/addproject", methods = ["GET", "POST"])
def addproject():
    form = ProjectForm()
    if form.validate_on_submit():
        image = form.img.data
        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))

        db.session.add(Project(
            name = form.name.data,
            content = request.form["content"],
            cover_image = image_name,
            date = datetime.datetime.now(),
            show_on_home = "show_on_home" in request.form,
            profession_id = request.form["category"]
        ))
        db.session.commit()
        return redirect(url_for("portfolio"))
    template = render_template("admin/portfolio/projects/addproject.html", professions = Profession.query.all(), form = form)
    return checkLogin(template)

@app.route("/admin/updateproject/<id>", methods = ["GET", "POST"])
def updateproject(id):
    project = Project.query.get(int(id))
    professions = Profession.query.all()
    selected_profession = Profession.query.get(project.profession_id)
    form = ProjectForm()
    if form.validate_on_submit():
        project.name = form.name.data
        project.content = request.form["content"]
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], project.cover_image)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], project.cover_image))
        image = form.img.data
        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))
        project.cover_image = image_name
        project.show_on_home = "show_on_home" in request.form
        project.profession_id = request.form["profession"]
        db.session.commit()
        return redirect(url_for("portfolio"))
    template = render_template("admin/portfolio/projects/updateproject.html", project = project, professions = professions, selected_profession = selected_profession, form = form)
    return checkLogin(template)

@app.route("/admin/deleteproject/<id>")
def deleteproject(id):
    db.session.delete(Project.query.get(int(id)))
    db.session.commit()
    template = redirect("/admin/portfolio")
    return checkLogin(template)

# Project image
@app.route("/admin/addprojectimage", methods = ["GET", "POST"])
def addprojectimage():
    form = ProjectImageForm()
    if form.validate_on_submit():
        image = form.img.data
        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))

        db.session.add(Project_image(
            image = image_name,
            project_id = request.form["project"]
        ))
        db.session.commit()
        return redirect(url_for("portfolio"))
    template = render_template("admin/design-project/images/addimage.html", projects = Project.query.all(), form = form)
    return checkLogin(template)
    
@app.route("/admin/updateprojectimage/<id>", methods = ["GET", "POST"])
def updateprojectimage(id):
    projects = Project.query.all()
    project_image = Project_image.query.get(int(id))
    selected_project = Project.query.get(project_image.project_id)
    form = ProjectImageForm()
    if form.validate_on_submit():
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], project_image.image)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], project_image.image))
        image = form.img.data
        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))
        project_image.image = image_name
        project_image.project_id = request.form["project"]
        db.session.commit()
        return redirect("/admin/portfolio")
    template = render_template("admin/design-project/images/updateimage.html", projects = projects, 
    form = form, selected_project = selected_project)
    return checkLogin(template)

@app.route("/admin/deleteprojectimage/<id>")
def deleteprojectimage(id):
    db.session.delete(Project_image.query.get(int(id)))
    db.session.commit()
    template = redirect("/admin/portfolio")
    return checkLogin(template)


# About page
@app.route("/admin/about")
def about():
    about = About_page.query.first()
    social_medias = Social_media.query.all()
    template = render_template("admin/about/about.html", about = about, social_medias = social_medias)
    return checkLogin(template)

@app.route("/admin/updateaboutpage", methods = ["GET", "POST"])
def updateaboutpage():
    about_page = About_page.query.get(1)
    form = AboutPageForm()
    if form.validate_on_submit():
        about_page.title = form.title.data
        about_page.content = request.form["content"]
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], about_page.image)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], about_page.image))
        image = form.img.data
        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))
        about_page.image = image_name
        db.session.commit()
        return redirect(url_for("about"))
    template = render_template("admin/about/updateabout.html", about_page = about_page, form = form)
    return checkLogin(template)


# Contact page
@app.route("/admin/contact")
def contact():
    contact_page = Contact_page.query.first()
    contacts = Contact.query.all()
    user_messages = User_message.query.all()
    template = render_template("admin/contact/contactpage.html", contact_page = contact_page, contacts = contacts, user_messages = user_messages)
    return checkLogin(template)

@app.route("/admin/updatecontactpage", methods = ["GET", "POST"])
def updatecontactpage():
    contact_page = Contact_page.query.get(1)
    form = ContactPageForm()
    if form.validate_on_submit():
        contact_page.title1 = form.title1.data
        contact_page.title2 = form.title2.data
        if form.img.data:
            if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], contact_page.image)):
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], contact_page.image))
            image = form.img.data
            image_name = secure_filename(image.filename)
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))
            contact_page.image = image_name
        else:
            contact_page.image = ""
        db.session.commit()
        return redirect("/admin/contact")
    template = render_template("admin/contact/contactpage/updatecontactpage.html", contact_page = contact_page, form = form)
    return checkLogin(template)

@app.route("/admin/addcontact", methods = ["GET", "POST"])
def addcontact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            name = form.name.data,
            value = form.value.data,
            show_on_footer = "show_on_footer" in request.form,
            show_on_contact = "show_on_contact" in request.form
        )
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for("addcontact"))
    template = render_template("admin/contact/contacts/addcontact.html", form = form)
    return checkLogin(template)

@app.route("/admin/updatecontact/<id>", methods = ["GET", "POST"])
def updatecontact(id):
    contact = Contact.query.get(int(id))
    form = ContactForm()
    if form.validate_on_submit():
        contact.name = form.name.data
        contact.value = form.value.data
        contact.show_on_footer = "show_on_footer" in request.form
        contact.show_on_contact = "show_on_contact" in request.form
        db.session.commit()
        return redirect(url_for("contact"))
    template = render_template("admin/contact/contacts/updatecontact.html", contact = contact, form = form)
    return checkLogin(template)

@app.route("/admin/deletecontact/<id>")
def deletecontact(id):
    db.session.delete(Contact.query.get(int(id)))
    db.session.commit()
    template = redirect("/admin/contact")
    return checkLogin(template)


# Social Media
@app.route("/admin/addsocialmedia", methods = ["GET", "POST"])
def addsocialmedia():
    if request.method == "POST":
        social_media = Social_media(
            name = request.form["name"],
            link = request.form["link"],
            icon_url = request.form["icon_url"],
            show_on_home = "show_on_home" in request.form,
            show_on_footer = "show_on_footer" in request.form,
            show_on_project = "show_on_project" in request.form,
            show_on_about = "show_on_about" in request.form
        )
        db.session.add(social_media)
        db.session.commit()
        return redirect("/admin/addsocialmedia")
    template = render_template("admin/socialmedias/addsocialmedia.html")
    return checkLogin(template)

@app.route("/admin/updatesocialmedia/<id>", methods = ["GET", "POST"])
def updatesocialmedia(id):
    social_media = Social_media.query.get(int(id))
    if request.method == "POST":
        social_media.name = request.form["name"]
        social_media.link = request.form["link"]
        social_media.show_on_home = "show_on_home" in request.form
        social_media.show_on_footer = "show_on_footer" in request.form
        social_media.show_on_project = "show_on_project" in request.form
        social_media.show_on_about = "show_on_about" in request.form
        db.session.commit()
        return redirect("/admin/about")
    template = render_template("admin/socialmedias/updatesocialmedia.html", social_media = social_media)
    return checkLogin(template)

@app.route("/admin/deletesocialmedia/<id>")
def deletesocialmedia(id):
    db.session.delete(Social_media.query.get(int(id)))
    db.session.commit()
    template = redirect("/admin/about")
    return checkLogin(template)