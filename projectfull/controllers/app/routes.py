from app import app
from flask import redirect, render_template, url_for
from model import db, Slider, About, Info, Employer, Profession, Skill, Project, About_page, Contact_page, Contact, User_message, Social_media
from form import UserMessageForm
import datetime

@app.route("/")
def index():
    employers = Employer.query.all()
    slides = Slider.query.all()
    about = About.query.first()
    projects = Project.query.filter_by(show_on_home = 1)
    infoList = Info.query.all()
    professions = Profession.query.all()
    skills = Skill.query.all()
    home_social_medias = Social_media.query.filter_by(show_on_home=1)
    footer_social_medias = Social_media.query.filter_by(show_on_footer=1)
    contacts = Contact.query.filter_by(show_on_footer = 1)
    return render_template("app/index.html", slides = slides, about = about, infoList = infoList, 
    projects = projects, employers = employers, Profession = Profession, professions = professions, skills = skills, 
    home_social_medias = home_social_medias, footer_social_medias = footer_social_medias, contacts = contacts)


@app.route("/portfolio")
def app_portfolio():
    projects = Project.query.all()
    professions = Profession.query.all()
    footer_social_medias = Social_media.query.filter_by(show_on_footer=1)
    contacts = Contact.query.filter_by(show_on_footer = 1)
    return render_template("app/portfolio.html", projects = projects, Profession = Profession, 
    professions = professions, footer_social_medias = footer_social_medias, contacts = contacts)


@app.route("/about")
def app_about():
    about_page = About_page.query.first()
    about_social_medias = Social_media.query.filter_by(show_on_about = 1)
    footer_social_medias = Social_media.query.filter_by(show_on_footer=1)
    contacts = Contact.query.filter_by(show_on_footer = 1)
    return render_template("app/about.html", about_page = about_page, about_social_medias = about_social_medias,
    footer_social_medias = footer_social_medias, contacts = contacts)

@app.route("/contact", methods = ["GET", "POST"])
def app_contact():
    contact_page = Contact_page.query.first()
    contacts_for_page = Contact.query.filter_by(show_on_contact = 1)
    footer_social_medias = Social_media.query.filter_by(show_on_footer=1)
    contacts = Contact.query.filter_by(show_on_footer = 1)
    form = UserMessageForm()
    if form.validate_on_submit():
        db.session.add(User_message(
            name = form.name.data,
            email = form.email.data,
            message = form.message.data,
            date = datetime.datetime.now()
        ))
        db.session.commit()
        return redirect(url_for("app_contact"))
    return render_template("app/contact.html", contact_page = contact_page, contacts_for_page = contacts_for_page, form = form,
    footer_social_medias = footer_social_medias, contacts = contacts)


@app.route("/project<id>")
def app_project(id):
    project = Project.query.get(int(id))
    project_social_medias = Social_media.query.filter_by(show_on_project = 1)
    footer_social_medias = Social_media.query.filter_by(show_on_footer=1)
    contacts = Contact.query.filter_by(show_on_footer = 1)
    return render_template("app/design-project.html", project = project, Project = Project,
    Profession = Profession, project_social_medias = project_social_medias, 
    footer_social_medias = footer_social_medias, contacts = contacts)

@app.route("/portfolio<int:id>")
def portfoliofilter(id):
    professions = Profession.query.all()
    projects = Project.query.filter_by(profession_id = id)
    footer_social_medias = Social_media.query.filter_by(show_on_footer=1)
    contacts = Contact.query.filter_by(show_on_footer = 1)
    return render_template("app/portfolio.html", projects = projects, Profession = Profession, 
    professions = professions, footer_social_medias = footer_social_medias, contacts = contacts)
