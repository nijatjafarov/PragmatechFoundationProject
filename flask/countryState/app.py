from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///countrystate.db"
db = SQLAlchemy(app)

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    states = db.relationship("State", backref="country", lazy=True)

class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey("country.id"), nullable=False)


@app.route("/", methods=['GET', "POST"])
def index():
    countries = Country.query.all()
    country_id = request.form.get("country")
    return f'{country_id}'
    states = State.query.filter_by(country_id=country_id).all()
    return render_template("index.html", countries = countries, states = states)

@app.route("/addcountry", methods=["GET", "POST"])
def addcountry():
    if request.method == "POST":
        db.session.add(Country(name = request.form["country"]))
        db.session.commit()
        return redirect("/addcountry")
    return render_template("country.html")

@app.route("/addstate", methods = ["GET", "POST"])
def addstate():
    countries = Country.query.all()
    if request.method == "POST":
        db.session.add(State(name = request.form["state"], country_id = int(request.form["country"])))
        db.session.commit()
        return redirect("/addstate")
    return render_template("state.html", countries = countries)

@app.route("/database")
def database():
    countries = Country.query.all()
    states = State.query.all()
    return render_template("database.html", countries = countries, states = states)

if __name__ == "__main__":
    app.run(debug=True)