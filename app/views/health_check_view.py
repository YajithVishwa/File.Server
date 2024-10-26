from flask import Blueprint
from ..main import health_check

health_check_blueprint = Blueprint('healthCheck', __name__)

@health_check_blueprint.route('/api/health', methods=['GET'])
def health():
    return health_check()
