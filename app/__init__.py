# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import routes and register blueprints
        from .views import list_directory_view, create_directory_view, delete_directory_view
        app.register_blueprint(list_directory_view.list_directory_blueprint)
        app.register_blueprint(create_directory_view.create_directory_blueprint)
        app.register_blueprint(delete_directory_view.delete_directory_blueprint)

    return app
