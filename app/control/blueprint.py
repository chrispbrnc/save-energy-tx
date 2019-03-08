from flask import Blueprint
from flask_admin import Admin
from app.control.views import AdminView

class AdminBlueprint(Blueprint):
    views=None

    def __init__(self, *args, **kwargs):
        self.views = []
        return super(AdminBlueprint, self).__init__('admin2',
            __name__, url_prefix='/admin', static_folder='static',
            static_url_path='/static/admin')

    def add_view(self, view):
        self.views.append(view)

    def register(self, app, options, first_registration=False):
        print(app)
        admin = Admin(app, name='Energy Saver of Texas', template_mode='bootstrap3', index_view=AdminView())
        for v in self.views:
            admin.add_view(v)

        return super(AdminBlueprint, self).register(app, options, first_registration)
