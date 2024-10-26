from flask import Blueprint, jsonify, request
from ..models.MetaDataDirectory import MetaDataDirectory
from ..main import health_check

metadata_directory_blueprint = Blueprint('metadataDirectory', __name__)

@metadata_directory_blueprint.route('/api/get-status', methods=['GET'])
def metadata_dir():
    data = request.get_json()
    if not data or 'path' not in data:
        return jsonify({"error": "Path parameter is required"}), 400
    path = data['path']
    metadata_directory_model = MetaDataDirectory(path)
    result = metadata_directory_model.get_metadata()
    if "Error" in result:
        return result, 400
    return result, 200
