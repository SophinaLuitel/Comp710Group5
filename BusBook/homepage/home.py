from flask import Blueprint, render_template

pages = Blueprint("home", __name__ , static_folder = "/static", template_folder = "/templates")
@pages.route("/")
def homepage():
    return render_template("index.html")

#@account.route("/bookings")
