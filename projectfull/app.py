from flask import Flask
app = Flask(__name__)

from controllers.app.routes import *
from controllers.admin.routes import *
from model import db, Slider, About, Info, Employer, Profession, Skill, Project, Project_image

if __name__ == "__main__":
    app.run(debug=True)