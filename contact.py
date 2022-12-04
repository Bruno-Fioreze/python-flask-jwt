from flask import Blueprint, render_template

bp = Blueprint("contact", __name__, url_prefix="/contact")


@bp.route("/")
def contact():
    return render_template("index.html")


def configure(app):
    app.register_blueprint(bp)
