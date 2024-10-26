import os
from flask import jsonify

class ListDirectoryModel:
    def __init__(self, path):
        self.path = path
        self.contents = self._list_directory_contents(path)

    def _list_directory_contents(self, path):
        try:
            content = {}
            if os.path.isdir(path):
                for item in os.listdir(path):
                    item_path = os.path.join(path, item)
                    if os.path.isdir(item_path):
                        content[item] = self._list_directory_contents(item_path)
                    else:
                        content.setdefault('files', []).append(item)
            else:
                if os.path.exists(path):
                    return {'file': os.path.basename(path)}
                else:
                    return {"Error": "File/Directory not found"}
            return content
        except Exception as e:
            return {"Error": str(e)}

    def get_content(self):
        return self.contents
