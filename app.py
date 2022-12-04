from flask import Flask
import views, contact


def create_app():
    app = Flask(__name__)
    views.configure(app)
    contact.configure(app)
    return app
