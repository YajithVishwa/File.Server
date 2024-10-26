# app/__init__.py
from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    print(app.config['UPLOAD_FOLDER'])
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    with app.app_context():
        # Import routes and register blueprints
        from .views import health_check_view,list_directory_view, create_directory_view, delete_directory_view, metadata_directory_view, upload_file_view, copy_directory_view, move_directory_view, download_directory_view
        app.register_blueprint(health_check_view.health_check_blueprint)
        app.register_blueprint(list_directory_view.list_directory_blueprint)
        app.register_blueprint(create_directory_view.create_directory_blueprint)
        app.register_blueprint(delete_directory_view.delete_directory_blueprint)
        app.register_blueprint(metadata_directory_view.metadata_directory_blueprint)
        app.register_blueprint(upload_file_view.upload_directory_blueprint)
        app.register_blueprint(copy_directory_view.copy_directory_blueprint)
        app.register_blueprint(move_directory_view.move_directory_blueprint)
        app.register_blueprint(download_directory_view.download_directory_blueprint)
    return app
