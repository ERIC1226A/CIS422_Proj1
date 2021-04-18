"""
Author: Connor Finch
Created on: 4/16/2021
Database: Takes in user input from a website and organizes it into a dictionary database

TODO: Compile user input into a dictionary/database

$env:FLASK_APP = "main.py"


"""

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    job = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"first name = {self.first_name}, last name = {self.last_name}, city = {self.city}, state = {self.state}, address = {self.address}, job = {self.job}"

@app.route("/")
def index():
    title = "TITLE GOES HERE"
    return render_template("index.html", title=title)

@app.route("/userform")
def userform():
    title = "userform"
    return render_template("userform.html",title=title)

@app.route("/database", methods=["POST","GET"])
def database():
    title = "database"
    fn = request.form.get("fname")
    ln = request.form.get("lname")
    city = request.form.get("city")
    state = request.form.get("state")
    address = request.form.get("address")
    job = request.form.get("job")


    if request.method == "POST":
        new_user = User(first_name=fn, last_name=ln, city=city, state=state, address=address, job=job)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect("/database")
        except:
            return "FAILED TO ADD USER TO DATABASE"
    else:
        all_users = User.query.order_by(User.date_created)
        return render_template("database.html",title=title, users=all_users)



if __name__ == "__main__":
    app.run()