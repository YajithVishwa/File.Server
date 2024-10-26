import os
from flask import jsonify, send_file

class DownloadFileModel:
    def __init__(self, path):
        self.path = path

    def dowload_file(self):
        try:
            if not os.path.exists(self.path):
                raise Exception('File not found')
            return send_file(self.path, as_attachment=True)
        except Exception as e:
            return {"status" : "False", "Error": str(e)}
