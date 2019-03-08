from flask_admin.contrib.sqla import ModelView
from app.control.blueprint import AdminBlueprint as Blueprint
from app.models.user import User

bp = Blueprint('admin', __name__)
