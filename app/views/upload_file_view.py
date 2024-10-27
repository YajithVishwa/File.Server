from flask import Blueprint, jsonify, request, flash
from ..models.UploadFile import UploadFileModel
from ..main import health_check

upload_directory_blueprint = Blueprint('uploadDirectory', __name__)

@upload_directory_blueprint.route('/api/put', methods=['POST'])
def upload_dir():
    data = request.form
    if 'file' not in request.files:
        flash("No file part")
        return jsonify({"Error": "File is required"}), 400
    file = request.files['file']
    if not data or 'path' not in data:
        return jsonify({"Error": "Path parameter is required"}), 400
    path = data['path']
    if file.filename == '':
        flash("No selected file")
        return jsonify({"Error": "File is required"}), 400
    overwrite = True
    if 'overwrite' in data:
        overwrite = data['overwrite'] 
    try:
        upload_directory_model = UploadFileModel(path, file, overwrite)
        result = upload_directory_model.upload_file()
        if "Error" in result:
            return result, 400
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    return result, 200
