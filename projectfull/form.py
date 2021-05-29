from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextField, IntegerField, TextAreaField, BooleanField
from wtforms import validators
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from model import bcrypt, Contact, Employer, Profession, Project, Project_image, Slider, About, Info
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    adminname = TextField("Adminname", validators=[DataRequired(), Length(max=20)])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")

    def validate_adminname(self, adminname):
        adminname = adminname.data
        if adminname != "hello":
            raise ValidationError('Wrong adminname')

class SliderForm(FlaskForm):
    img = FileField("Choose an image", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

    def validate_img(self, img):
        image = Slider.query.filter_by(image = img.data.filename).first()
        #Bununla eyni deyilse
        if image:
            raise ValidationError('This image is chosen. Choose again.')


class AboutForm(FlaskForm):
    title = TextField("Title", validators=[DataRequired(), Length(max=30)])
    content = TextAreaField("Content", validators=[DataRequired()], default=About.query.first().content)


class InfoForm(FlaskForm):
    name = TextField("Name", validators=[DataRequired(), Length(max=30)])
    value = IntegerField("Value", validators=[DataRequired()])

    def validate_name(self, name):
        info = Info.query.filter_by(name = name.data).first()
        if info:
            raise ValidationError('This name is chosen. Choose again.')

class EmployerForm(FlaskForm):
    fullname = TextField("Fullname", validators=[DataRequired(), Length(max=25)])
    profession = TextField("Profession", validators=[DataRequired(), Length(max=35)])
    img = FileField("Choose a photo", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

    def validate_img(self, img):
        photo = Employer.query.filter_by(photo = img.data.filename).first()
        if photo:
            raise ValidationError('This image is chosen. Choose again.')

class ProfessionForm(FlaskForm):
    name = TextField("Name", validators=[DataRequired(), Length(max=30)])
    description = TextField("Short description", validators=[DataRequired(), Length(max=120)])
    img = FileField("Choose an image", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

    def validate_name(self, name):
        name = Profession.query.filter_by(name = name.data).first()
        if name:
            raise ValidationError('This name is chosen. Choose again.')

    def validate_description(self, description):
        description = Profession.query.filter_by(description = description.data).first()
        if description:
            raise ValidationError('This is not a unique description')

    def validate_img(self, img):
        image = Profession.query.filter_by(image = img.data.filename).first()
        if image:
            raise ValidationError('This image is chosen. Choose again.')

class SkillForm(FlaskForm):
    skill = TextField("Skill", validators=[DataRequired(), Length(max=70)])

class ProjectForm(FlaskForm):
    name = TextField("Name", validators=[DataRequired(), Length(max=50)])
    img = FileField("Choose a cover image", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

    def validate_name(self, name):
        name = Project.query.filter_by(name = name.data).first()
        if name:
            raise ValidationError('This name is chosen. Choose again.')
    
    def validate_img(self, img):
        image = Project.query.filter_by(cover_image = img.data.filename).first()
        if image:
            raise ValidationError('This image is chosen. Choose again.')

class ProjectImageForm(FlaskForm):
    img = FileField("Choose a cover image", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

    def validate_img(self, img):
        image = Project_image.query.filter_by(image = img.data.filename).first()
        if image:
            raise ValidationError('This image is chosen. Choose again.')

class AboutPageForm(FlaskForm):
    img = FileField("Choose an image", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    title = TextField("Update the title", validators=[DataRequired(), Length(max=80)])

class ContactPageForm(FlaskForm):
    title1 = TextField("Update the first title", validators=[Length(max=80)])
    title2 = TextField("Update the second title", validators=[Length(max=80)])
    img = FileField("Choose an image", validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

class ContactForm(FlaskForm):
    name = TextField("Name", validators=[DataRequired()])
    value = TextField("Value", validators=[DataRequired()])

    def validate_name(self, name):
        name = Contact.query.filter_by(name = name.data).first()
        if name:
            raise ValidationError('This name is chosen. Choose again.')

    def validate_value(self, value):
        value = Contact.query.filter_by(value = value.data).first()
        if value:
            raise ValidationError('This value is chosen. Choose again.')


class UserMessageForm(FlaskForm):
    name = TextField(validators=[DataRequired()])
    email = EmailField(validators=[DataRequired(), validators.Email()])
    message = TextField(validators=[DataRequired()])

class SocialMediaForm(FlaskForm):
    name = TextField("Name")
    icon_url = TextField("Icon UNICODE")
    link = TextField("Link", validators=[DataRequired()])
    show_on_home = BooleanField("Show this social media account on Sidebar on Home Page")
    show_on_footer = BooleanField("Show this social media account on Footer")
    show_on_project = BooleanField("Show this social media account on projects")
    show_on_about = BooleanField("Show this social media account on About Page")
    