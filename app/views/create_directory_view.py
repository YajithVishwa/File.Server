from flask import Blueprint, jsonify, request
from ..models.CreateDirectory import CreateDirectoryModel

create_directory_blueprint = Blueprint('CreateDirectory', __name__)

@create_directory_blueprint.route('/api/create', methods=['PUT'])
def create_dir():
    data = request.get_json()
    if not data or 'path' not in data:
        return jsonify({"error": "Path parameter is required"}), 400
    path = data['path']
    isFile = False
    if "isFile" in data:
        isFile = data['isFile']
    create_directory_model = CreateDirectoryModel(path, isFile)
    result = reate_directory_model.get_status()
    if "Error" in result:
        return result, 400
    return result, 200
