from flask import Flask, Blueprint

from myapp.authors import views


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app.run()


def register_blueprints(app: Flask):
    app.register_blueprint(views.author, url_prefix="/authors")    

