import config
from app.main import bp



@bp.route('/')
def index():
    return f"<h1>Go to URLSCAN</h1>"
