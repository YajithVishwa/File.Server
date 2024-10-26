from flask import Blueprint, jsonify, request
from ..models.ListDirectory import ListDirectoryModel
from ..main import health_check

list_directory_blueprint = Blueprint('listDirectory', __name__)

@list_directory_blueprint.route('/api/health', methods=['GET'])
def health():
    return health_check()

@list_directory_blueprint.route('/api/list', methods=['GET'])
def list_dir():
    data = request.get_json()
    if not data or 'path' not in data:
        return jsonify({"error": "Path parameter is required"}), 400
    path = data['path']
    list_directory_model = ListDirectoryModel(path)
    result = list_directory_model.get_content()
    if "Error" in result:
        return result, 400
    return result, 200
