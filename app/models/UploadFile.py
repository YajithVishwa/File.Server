import os
from flask import jsonify, current_app

class UploadFileModel:
    def __init__(self, path, file, overwrite='true'):
        self.root_fullPath = current_app.config['UPLOAD_FOLDER']
        self.path = path
        self.fullPath = self.root_fullPath + self.path
        self.file = file
        self.overwrite = overwrite

    def upload_file(self):
        try:
            if not os.path.exists(self.fullPath):
                os.makedirs(self.fullPath)
            else:
                if self.overwrite == 'false':
                    raise FileExistsError('File already there, use overwrite as True and try again')
            filename = self.file.filename
            filefullPath = os.path.join(self.fullPath, filename)
            self.file.save(filefullPath)
            fullPath = self.path + filename
            return {"status" : "True", "destination_path": fullPath}
        except FileExistsError as e:
            return {"status" : "False", "Error": str(e)}
