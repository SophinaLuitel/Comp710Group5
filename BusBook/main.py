from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from homepage.home import pages
from flightspage.flights import pages

app = Flask(__name__)

app.register_blueprint(pages,name='home1', url_prefix="/home")
app.register_blueprint(pages, name='flight1', url_prefix="/flights")
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    #db.create_all()
    app.run(debug=True)

