import os

from app.jira import jira, bp
from jira.client import ResultList, Issue

jira_url = os.getenv("SERVER")
jira_user = os.getenv("JIRA_USERNAME")
jira_password = os.getenv("PASSWORD")
client = jira.Jira(jira_server=jira_url, jira_username=jira_user, jira_password=jira_password)


@bp.route('/urlscan')
def URLScan():
    issues: ResultList[Issue] = client.getMyOpenIssues("URLSCAN")
    table = []

    for issue in issues:
        table.append({
            "Key":issue.key,
            "Summary": issue.get_field('summary'),
            "Status" : issue.get_field('status')
        })

    table = f'''<table><tr><th>key</th><th>Summary</th><th>Status</th></tr><tbody><tr><td>{table[0]["Key"]}</td><td>{table[0]["Summary"]}</td><td>{table[0]["Status"]}</td></tr></tbody></table>'''

    return table

