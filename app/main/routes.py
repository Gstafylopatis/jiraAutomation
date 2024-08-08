import config
from app.main import bp
import os


@bp.route('/')
def index():
    JIRA_USERNAME = os.getenv("JIRA_USERNAME")
    JIRA_PASSWORD = os.getenv("PASSWORD")

    return f"<h1>{JIRA_USERNAME}</h1>"
