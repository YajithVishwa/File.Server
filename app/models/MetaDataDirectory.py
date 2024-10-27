import os
from flask import jsonify, current_app
from datetime import datetime

class MetaDataDirectory:
    def __init__(self, path):
        self.root_fullPath = current_app.config['UPLOAD_FOLDER']
        self.path = path
        self.full_path = self.root_fullPath + self.path
        self.metadata = self._metadata_directory()

    def _convert_size(self, size_bytes):
        """Convert size in bytes to KB, MB, or GB."""
        if size_bytes < 1024:
            return f"{size_bytes} Bytes"
        elif size_bytes < 1024 ** 2:
            return f"{size_bytes / 1024:.2f} KB"
        elif size_bytes < 1024 ** 3:
            return f"{size_bytes / (1024 ** 2):.2f} MB"
        else:
            return f"{size_bytes / (1024 ** 3):.2f} GB"

    def _metadata_directory(self):
        try:
            if os.path.exists(self.full_path):
                if os.path.isfile(self.full_path):
                    total_size = os.path.getsize(self.full_path)
                    modification_time = os.path.getmtime(self.full_path)
                    modification_time_readable = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')
                    return {"total_size": self._convert_size(total_size) , "modification_time": modification_time_readable}
                else:
                    total_size = 0
                    file_count = 0
                    for dirpath, dirnames, filenames in os.walk(self.full_path):
                        for filename in filenames:
                            file_path = os.path.join(dirpath, filename)
                            total_size += os.path.getsize(file_path)
                            file_count += 1
                    modification_time = os.path.getmtime(self.full_path)
                    modification_time_readable = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')
                    return {"total_size": self._convert_size(total_size), "file_count": file_count, "modification_time": modification_time_readable}
            else:
                raise FileNotFoundError("File/Directory not found")
        except FileNotFoundError as e:
            return {"Error": str(e)}

    def get_metadata(self):
        return self.metadata
