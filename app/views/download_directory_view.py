from flask import Blueprint, jsonify, request
from ..models.DownloadFile import DownloadFileModel

download_directory_blueprint = Blueprint('DownloadDirectory', __name__)

@download_directory_blueprint.route('/api/get', methods=['GET'])
def copy_dir():
    data = request.form
    if 'path' not in data:
        return jsonify({"Error": "path parameter is required"}), 400
    path = data['path']
    try:
        download_directory_model = DownloadFileModel(path)
        result = download_directory_model.dowload_file()
        if isinstance(result, dict) and "Error" in result:
            return jsonify(result), 400
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    return result, 200
