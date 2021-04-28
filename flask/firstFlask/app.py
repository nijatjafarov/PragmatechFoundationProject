from flask import Flask, request, render_template, Markup

app = Flask(__name__)
people = []
class User:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname =surname
        self.city = city

@app.route("/", methods = ["GET", "POST"])
def index():
    
    if request.method == "POST":
        ad = request.form["ad"]
        soyad = request.form["soyad"]
        sheher = request.form["sheher"]
        people.append(User(ad, soyad, sheher))
    return render_template("index.html")

@app.route("/show")
def show():
    return render_template("show.html", people = people)

if __name__ == "__main__":
    app.run(debug=True)