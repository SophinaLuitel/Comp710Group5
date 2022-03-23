from Flask import Blueprint, render_template

account = Blueprint("home", __name__ , static_folder = "static", template_folder = "templates")
@account.route("/settings")


@account.route("/bookings")