import flask_admin as admin

class IndexView(admin.BaseView):
    @admin.expose('/')
    def index(self):
        return self.render('control/index.html')
