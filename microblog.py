from app import app
from app.models import db, User, Post

@app.shell_context_processor
def make_shell_content():
    return {'db': db, 'User': User, 'Post': Post}
