from flask import Flask, render_template, request, redirect

app = Flask(__name__)

books = []
bookId = 1
class Book:
    def __init__(self, _id, _name, _author, _price):
        self.id = _id
        self.name = _name
        self.author = _author
        self.price = _price

@app.route("/")
@app.route("/show")
def show():
    return render_template("show.html", books = books)

@app.route("/add", methods=["GET", "POST"])
def add():
    global bookId
    if request.method=='POST':
        bookName = request.form["name"]
        bookAuthor = request.form["author"]
        bookPrice = request.form["cost"]
        books.append(Book(bookId, bookName, bookAuthor, bookPrice))
        bookId += 1
        return render_template("add.html")
    return render_template("add.html")

@app.route("/delete/<int:id>", methods = ["GET"])
def delete(id):
    for book in books:
        if id == book.id:
            books.remove(book)
            return redirect("/")
    return redirect("/")

# @app.route("/update/<int:id>", methods = ["GET", "POST"])
# def update(id):
#     book = None
#     if request.method == "POST":
#         for i in range(len(books)):
#             if id == books[i].id:
#                 books[i].name = request.form["newName"]
#                 books[i].author = request.form["newAuthor"]
#                 books[i].price = request.form["newCost"]
#                 book = books[i]
#                 return redirect("/")
#     return render_template("update.html", book=books[0])


@app.route("/update/<int:id>", methods = ["GET", "POST"])
def update(id):
    for i in range(len(books)):
        if id == books[i].id:
            if request.method == "POST":
                books[i].name = request.form["newName"]
                books[i].author = request.form["newAuthor"]
                books[i].price = request.form["newCost"]
                return redirect("/")
            return render_template("update.html", book=books[i])
if __name__ == "__main__":
    app.run(debug=True)
