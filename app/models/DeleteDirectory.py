import os
from flask import jsonify

class DeleteDirectoryModel:
    def __init__(self, path, recursive=False):
        self.path = path
        self.recursive = recursive
        self.status = self._delete_directory(path)
    
    def check_files_in_folder(self, folder_path):
        for entry in os.listdir(folder_path):
            entry_path = os.path.join(folder_path, entry)
            if os.path.isfile(entry_path):
                return True
        return False
    
    def delete_files_recursively(self, folder_path):
        for entry in os.listdir(folder_path):
            entry_path = os.path.join(folder_path, entry)
            if os.path.isdir(entry_path):
                delete_folder_with_files(entry_path)
            else:
                os.remove(entry_path)
        os.rmdir(folder_path)

    def _delete_directory(self, path):
        try:
            if os.path.exists(path):
                if os.path.isfile(path):
                    os.remove(path)
                else:
                    if self.check_files_in_folder(self.path):
                        if self.recursive:
                            self.delete_files_recursively(self.path)
                        else:
                            raise Exception("Directory Contain Files, Add recursive as True and try again.")
                    else:
                        if not self.check_files_in_folder(self.path):
                            os.rmdir(path)
                        else:
                            raise Exception("Directory Contain Files, Add recursive as True and try again.")
            else:
                raise Exception('File/Directory not found')
            return {"status" : "True"}
        except Exception as e:
            return {"status" : "False", "Error": str(e)}

    def get_status(self):
        return self.status
