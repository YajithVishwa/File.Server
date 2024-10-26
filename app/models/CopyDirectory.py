import os
from flask import jsonify
import shutil

class CopyDirectoryModel:
    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        self.destination_path = destination_path
        self.status = self._copy_directory()

    def _copy_directory(self):
        try:
            os.makedirs(os.path.dirname(self.destination_path), exist_ok=True)
            shutil.copy(self.source_path, self.destination_path)
            return {"status" : "True", "destination_path": self.destination_path}
        except Exception as e:
            return {"status" : "False", "Error": str(e)}

    def get_status(self):
        return self.status
