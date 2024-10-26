from flask import Blueprint, jsonify, request
from ..models.DeleteDirectory import DeleteDirectoryModel

delete_directory_blueprint = Blueprint('DeleteDirectory', __name__)

@delete_directory_blueprint.route('/api/delete', methods=['DELETE'])
def create_dir():
    data = request.form
    if not data or 'path' not in data:
        return jsonify({"Error": "Path parameter is required"}), 400
    path = data['path']
    recursive = False
    if "recursive" in data:
        recursive = data['recursive']
    delete_directory_model = DeleteDirectoryModel(path, recursive)
    result = delete_directory_model.get_status()
    if "Error" in result:
        return result, 400
    return result, 200
