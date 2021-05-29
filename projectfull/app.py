from flask import Flask
app = Flask(__name__)
UPLOAD_FOLDER='static/app/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = "5791828bb0b13ce0c676dfde280ba245"

from controllers.app.routes import *
from controllers.admin.routes import *
from controllers.authentication.routes import *

if __name__ == "__main__":
    app.run(debug=True)