from flask import Blueprint, jsonify, request
from ..models.CopyDirectory import CopyDirectoryModel

copy_directory_blueprint = Blueprint('CopyDirectory', __name__)

@copy_directory_blueprint.route('/api/copy', methods=['POST'])
def copy_dir():
    data = request.form
    if not data or 'source_path' not in data:
        return jsonify({"Error": "source_path parameter is required"}), 400
    if 'destination_path' not in data:
        return jsonify({"Error": "destination_path parameter is required"}), 400
    source_path = data['source_path']
    destination_path = data['destination_path']
    
    copy_directory_model = CopyDirectoryModel(source_path, destination_path)
    result = copy_directory_model.get_status()
    if "Error" in result:
        return result, 400
    return result, 200
