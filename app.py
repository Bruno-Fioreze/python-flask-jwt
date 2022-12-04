from flask import Flask
import views, contact, db


def create_app():
    app = Flask(__name__)
    views.configure(app)
    contact.configure(app)
    # db.configure(app)
    return app
