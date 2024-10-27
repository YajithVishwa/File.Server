from flask import Blueprint, jsonify, request, current_app
from ..models.ListDirectory import ListDirectoryModel
from ..main import health_check

list_directory_blueprint = Blueprint('listDirectory', __name__)

@list_directory_blueprint.route('/api/list', methods=['GET'])
def list_dir():
    root_path = current_app.config['UPLOAD_FOLDER']
    data = request.form
    if 'path' not in data:
        path = root_path
        #return jsonify({"Error": "Path parameter is required"}), 400
    else:
        path = root_path+data['path']
    try:
        list_directory_model = ListDirectoryModel(path)
        result = list_directory_model.get_content()
        if "Error" in result:
            return result, 400
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    return result, 200
