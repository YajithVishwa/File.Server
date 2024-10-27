from flask import Blueprint, jsonify, request
from ..models.MoveDirectory import MoveDirectoryModel

move_directory_blueprint = Blueprint('MoveDirectory', __name__)

@move_directory_blueprint.route('/api/move', methods=['POST'])
def move_dir():
    data = request.form
    if not data or 'source_path' not in data:
        return jsonify({"Error": "source_path parameter is required"}), 400
    if 'destination_path' not in data:
        return jsonify({"Error": "destination_path parameter is required"}), 400
    source_path = data['source_path']
    destination_path = data['destination_path']
    try:
        move_directory_model = MoveDirectoryModel(source_path, destination_path)
        result = move_directory_model.get_status()
        if "Error" in result:
            return result, 400
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    return result, 200
