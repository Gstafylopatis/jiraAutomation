from jira import JIRA, Issue
from jira.client import ResultList


class Jira(object):

    def __init__(self, jira_server, jira_username, jira_password):
        self.jira_server = jira_server
        self.jira_username = jira_username
        self.jira_password = jira_password

        self.jira_client: JIRA = JIRA(server=jira_server, basic_auth=(jira_username, jira_password))

    def getIssue(self, issue_id: str) -> Issue:
        issue = self.jira_client.issue(id=issue_id)
        return issue

    def getMyOpenIssues(self, type='all', fields=None):
        # AND issuetype = '{issue_type}'
        jql = "project = TPGSOC  AND resolution = Unresolved AND assignee = 6388874a77acd224b34187ff"
        if type == "URLSCAN":
            jql += f" AND issuetype = 'Threat Intelligence'"

        my_open_issues: ResultList = self.jira_client.search_issues(jql_str=jql, expand=None, fields=fields)
        return my_open_issues
