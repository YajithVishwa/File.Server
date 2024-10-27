import os
from flask import jsonify, current_app

class CreateDirectoryModel:
    def __init__(self, path, isFile='False'):
        self.root_fullPath = current_app.config['UPLOAD_FOLDER']
        self.path = path
        self.full_path = self.root_fullPath + self.path
        self.isFile = isFile
        self.status = self._create_directory(path)

    def _create_directory(self, path):
        try:
            if os.path.exists(self.full_path):
                raise FileExistsError("File/Directory Already Exists")
            else:
                if self.isFile == 'True':
                    with open(self.full_path, 'w'):
                        pass
                else:
                    os.makedirs(self.full_path)
            return {"status" : "True"}
        except FileExistsError as e:
            return {"status" : "False", "Error": str(e)}

    def get_status(self):
        return self.status
