from flask import Blueprint, render_template

pages = Blueprint("flight123", __name__ , static_folder = "/static", template_folder = "/templates")
@pages.route("/search")
def homepage():
    return render_template("flights.html")

#@account.route("/bookings")
