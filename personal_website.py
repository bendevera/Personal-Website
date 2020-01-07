from app import APP, db
from app.models import Post, Block, Contact
import datetime

@APP.shell_context_processor
def make_shell_context():
    return {'db': db, 'Block': Block, 'Post': Post, 'Contact': Contact}

@APP.template_filter('prettytime')
def prettytime(s):
    return s.strftime('%b %d, %Y')
