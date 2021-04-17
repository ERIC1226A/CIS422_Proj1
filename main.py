"""
Author: Connor Finch
Created on: 4/16/2021
Database: Takes in user input from a website and organizes it into a dictionary database

TODO: Compile user input into a dictionary/database

$env:FLASK_APP = "main.py"


"""

from flask import Flask, render_template, request

app = Flask(__name__)

userinput = list()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form", methods=["POST"])
def form():

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    city = request.form.get("city")
    state = request.form.get("state")
    address = request.form.get("address")
    job = request.form.get("job")

    userinput.append(f"{fname}, {lname}, {city}, {state}, {address}, {job}")

    title = "TITLE GOES HERE"

    return render_template("form.html", title=title, userinput=userinput)
    #return render_template("form.html", title=title, fname=fname, lname=lname, city=city, state=state, address=address, job=job)

app.run()