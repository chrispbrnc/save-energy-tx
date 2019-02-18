from app import db, cli, create_app
from app.models import user

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': user.User,
    }
