import os
from flask import jsonify, send_file, current_app

class DownloadFileModel:
    def __init__(self, path):
        self.root_fullPath = current_app.config['UPLOAD_FOLDER']
        self.path = path
        self.full_path = self.root_fullPath + self.path

    def dowload_file(self):
        try:
            if not os.path.exists(self.full_path):
                raise Exception('File not found')
            return send_file(self.full_path, as_attachment=True)
        except Exception as e:
            return {"status" : "False", "Error": str(e)}
