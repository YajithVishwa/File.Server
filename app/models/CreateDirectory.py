import os
from flask import jsonify

class CreateDirectoryModel:
    def __init__(self, path, isFile=False):
        self.path = path
        self.isFile = isFile
        self.status = self._create_directory(path)

    def _create_directory(self, path):
        try:
            if os.path.exists(path):
                raise Exception("File/Directory Already Exists")
            else:
                if self.isFile:
                    with open(path, 'w'):
                        pass
                else:
                    os.mkdir(path)
            return {"status" : "True"}
        except Exception as e:
            return {"status" : "False", "Error": str(e)}

    def get_status(self):
        return self.status
