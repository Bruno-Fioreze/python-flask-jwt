from flask import jsonify


def configure(app):
    @app.route("/")
    def api():
        return "<p>Hello, World!</p>"
