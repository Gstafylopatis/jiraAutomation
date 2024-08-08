import config
from app.main import bp
import app.jira as Jira
from jira import Issue


@bp.route('/')
def index():
    client = Jira.create_jira_client()
    issue: Issue = client.getIssue("TPGSOC-499056")
    print(dict(issue.raw))
    resolution = issue.fields.resolution.description
    print(resolution)
    return f"<h1>{resolution}</h1>"
