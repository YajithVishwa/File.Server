from flask import Blueprint, jsonify, request
from ..models.DeleteDirectory import DeleteDirectoryModel

delete_directory_blueprint = Blueprint('DeleteDirectory', __name__)

@delete_directory_blueprint.route('/api/delete', methods=['DELETE'])
def create_dir():
    data = request.form
    if not data or 'path' not in data:
        return jsonify({"Error": "Path parameter is required"}), 400
    path = data['path']
    recursive = 'false'
    if "recursive" in data:
        recursive = data['recursive'].lower()
    try:
        delete_directory_model = DeleteDirectoryModel(path, recursive)
        result = delete_directory_model.get_status()
        if "Error" in result:
            return result, 400
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    return result, 200
