import os
from flask import jsonify

class UploadFileModel:
    def __init__(self, path, file, overwrite=True):
        self.path = path
        self.file = file
        self.overwrite = overwrite

    def upload_file(self):
        try:
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            else:
                if self.overwrite == 'False':
                    raise Exception('File already there, use overwrite as True and try again')
            filename = self.file.filename
            filepath = os.path.join(self.path, filename)
            self.file.save(filepath)
            return {"status" : "True", "path": filepath}
        except Exception as e:
            return {"status" : "False", "Error": str(e)}
