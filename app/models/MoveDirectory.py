import os
from flask import jsonify, current_app
import shutil

class MoveDirectoryModel:
    def __init__(self, source_path, destination_path):
        self.root_fullPath = current_app.config['UPLOAD_FOLDER']
        self.source_path = source_path
        self.full_source_path = self.root_fullPath + self.source_path
        self.destination_path = destination_path
        self.full_destination_path = self.root_fullPath + self.destination_path
        self.status = self._move_directory()

    def _move_directory(self):
        try:
            os.makedirs(os.path.dirname(self.full_destination_path), exist_ok=True)
            shutil.move(self.full_source_path, self.full_destination_path)
            return {"status" : "True", "destination_path": self.destination_path}
        except Exception as e:
            return {"status" : "False", "Error": str(e)}

    def get_status(self):
        return self.status
