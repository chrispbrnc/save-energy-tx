import flask_admin as admin
from flask import redirect, url_for
from flask_login import current_user, login_user, logout_user
from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.is_admin
        return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))


class AdminView(admin.AdminIndexView):
    @admin.expose('/')
    def index(self):
        if current_user.is_authenticated:
            if current_user.is_admin:
                return self.render('control/index.html')
        return redirect(url_for('auth.login'))

    @admin.expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login_user(user)

        if current_user.is_authenticated and current_user.is_admin:
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(AdminView, self).index()

    @admin.expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))
