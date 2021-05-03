from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shipping.db"
UPLOAD_FOLDER = "./static/uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
db = SQLAlchemy(app)

class Address(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(15), nullable = False)
    lname = db.Column(db.String(15), nullable = False)
    username = db.Column(db.String(30), unique=True, nullable = False)
    email = db.Column(db.String(100), unique=True, nullable = False)
    address = db.Column(db.Text, nullable = False)
    address2 = db.Column(db.Text)
    country = db.Column(db.String(20), nullable = False)
    state = db.Column(db.String(20), nullable = False)
    zip_code = db.Column(db.String(10), nullable = False)
    ship_billing_id = db.Column(db.Boolean)
    save_info = db.Column(db.Boolean)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    payment_option = db.Column(db.String(20))
    name_on_card = db.Column(db.String(20), nullable = False)
    card_number = db.Column(db.String(19), nullable = False)
    expiration = db.Column(db.String(5), nullable = False)
    cvv = db.Column(db.String(3), nullable = False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(15), nullable = False)
    short_desc = db.Column(db.String(60), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    image = db.Column(db.String(100))
    date = db.Column(db.String(100))

@app.route("/", methods = ["GET", "POST"])
def index():
    products = Product.query.all()
    total= len(products)
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        username = request.form["username"]
        email = request.form["email"]
        address = request.form["address"]
        address2 = request.form["address2"]
        country = request.form["country"]
        state = request.form["state"]
        zip_code = request.form["zip"]
        ship_billing_id = "ship_bill_id" in request.form
        save_info = "save_info" in request.form
        address = Address(fname=fname, lname=lname, username=username, email=email, address=address, address2=address2, country=country, state=state, zip_code=zip_code, ship_billing_id=ship_billing_id, save_info=save_info)
        db.session.add(address)

        payment_option = request.form["payment_option"]
        name_on_card = request.form["name_on_card"]
        card_number = request.form["card_number"]
        expiration = request.form["expiration"]
        cvv = request.form["cvv"]
        payment = Payment(payment_option=payment_option, name_on_card=name_on_card, card_number=card_number, expiration=expiration, cvv=cvv)
        db.session.add(payment)

        db.session.commit()
        return redirect("/show")
    return render_template("index.html", products=products, total=total)

@app.route("/show")
def show():
    addresses = Address.query.all()
    payments = Payment.query.all()
    return render_template("show.html", addresses = addresses, payments = payments)

@app.route("/products")
def products():
    products = Product.query.all()
    return render_template("products.html", products = products)

@app.route("/addproduct", methods = ["GET", "POST"])
def add_product():
    if request.method == "POST":
        
        name = request.form["name"]
        short_desc = request.form["short_desc"]
        price = request.form["price"]
        uploaded_file = request.files['image']
        APP_ROOT = os.path.dirname(os.path.abspath(__file__))
        UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        uploaded_file.save(os.path.join(UPLOAD_FOLDER),uploaded_file.filename)
        datetime = str(datetime.datetime.utcnow)
        product = Product(name=name, short_desc=short_desc, price=price, image=uploaded_file.filename, date=date)
        db.session.add(product)
        db.session.commit()
        return redirect("/products")
    return render_template("addproduct.html")

if __name__ == "__main__":
    app.run(debug=True)