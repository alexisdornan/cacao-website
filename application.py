from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions

from helpers import apology, lookup

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///signup.db")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/events", methods=["GET"])
def events():
    return render_template("events.html")


@app.route("/founders", methods=["GET"])
def founders():
    return render_template("founders.html")


@app.route("/mission", methods=["GET"])
def mission():
    return render_template("mission.html")


@app.route("/donate", methods=["GET"])
def donate():
    return render_template("donate.html")


@app.route("/info", methods=["GET"])
def info():
    return render_template("info.html")


@app.route("/confirmed", methods=["GET"])
def confirmed():
    return render_template("confirmed.html")


@app.route("/recipe", methods=["GET", "POST"])
def recipe():
    """Returns recipe list"""
    if request.method == "POST":
        ing = request.form.get("ing")
        if not ing:
            return apology("Missing Ingredient!")
        values = lookup(ing)
        return render_template("recipe.html", values=values)

    else:
        return render_template("recipe.html")


@app.route("/emailregister", methods=["GET", "POST"])
def emailregister():
    """Register email for user"""
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        confirmation_email = request.form.get("confirmation")
        if not name:
            return apology("Missing Name!")

        if not email:
            return apology("Missing Email!")

        if email[(len(email) - 9):] != "@yale.edu":
            return apology("Please Enter a Yale Email!")

        if not confirmation_email:
            return apology("Missing Confirmation Email!")

        if email != confirmation_email:
            return apology("Email and Confirmation Email Do Not Match!")

        result = db.execute("INSERT INTO email (email, name) VALUES(:email, :name)",
                            email=request.form.get("email"), name=request.form.get("name"))
        if not result:
            # the email already exists in the database
            return apology("Please enter a different email as the one entered has already been taken")
        return redirect("/confirmed")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("emailregister.html")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
