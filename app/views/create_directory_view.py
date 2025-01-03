from flask import Blueprint, jsonify, request
from ..models.CreateDirectory import CreateDirectoryModel

create_directory_blueprint = Blueprint('CreateDirectory', __name__)

@create_directory_blueprint.route('/api/create', methods=['PUT'])
def create_dir():
    data = request.form
    if not data or 'path' not in data:
        return jsonify({"Error": "Path parameter is required"}), 400
    path = data['path']
    isFile = 'false'
    if "isFile" in data:
        isFile = data['isFile'].lower()
    try:
        create_directory_model = CreateDirectoryModel(path, isFile)
        result = create_directory_model.get_status()
        if "Error" in result:
            return result, 400
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    return result, 200
