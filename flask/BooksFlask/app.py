from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    author = db.Column(db.String(30), nullable = False)
    price = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Book('{self.name}', '{self.author}', '{self.price}')"

@app.route("/")
@app.route("/show")
def show():
    books = Book.query.all()
    return render_template("show.html", books = books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method=='POST':
        bookName = request.form["name"]
        bookAuthor = request.form["author"]
        bookPrice = int(request.form["cost"])
        book = Book(name=bookName, author=bookAuthor, price=bookPrice)
        db.session.add(book)
        db.session.commit()
        return render_template("add.html")
    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete(id):
    db.session.delete(Book.query.get(id))
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:id>", methods = ["GET", "POST"])
def update(id):
    book = Book.query.get(id)
    if request.method == "POST":
        book.name = request.form["newName"]
        book.author = request.form["newAuthor"]
        book.price = request.form["newCost"]
        db.session.commit()
        return redirect("/")
    return render_template("update.html", book=book)

if __name__ == "__main__":
    app.run(debug=True)
