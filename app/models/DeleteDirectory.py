import os
from flask import jsonify, current_app

class DeleteDirectoryModel:
    def __init__(self, path, recursive='False'):
        self.root_fullPath = current_app.config['UPLOAD_FOLDER']
        self.path = path
        self.full_path = self.root_fullPath + self.path
        self.recursive = recursive
        self.status = self._delete_directory()
    
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

    def _delete_directory(self):
        try:
            if os.path.exists(self.full_path):
                if os.path.isfile(self.full_path):
                    os.remove(self.full_path)
                else:
                    if self.check_files_in_folder(self.full_path):
                        if self.recursive == 'True':
                            self.delete_files_recursively(self.full_path)
                        else:
                            raise Exception("Directory Contain Files, Add recursive as True and try again.")
                    else:
                        if not self.check_files_in_folder(self.full_path):
                            os.rmdir(self.full_path)
                        else:
                            raise Exception("Directory Contain Files, Add recursive as True and try again.")
            else:
                raise Exception('File/Directory not found')
            return {"status" : "True"}
        except Exception as e:
            return {"status" : "False", "Error": str(e)}

    def get_status(self):
        return self.status
