from jira import JIRA, Issue


class Jira(object):

    def __init__(self, jira_server, jira_username, jira_password):
        self.jira_server = jira_server
        self.jira_username = jira_username
        self.jira_password = jira_password

        self.jira_client = JIRA(server=jira_server, basic_auth=(jira_username, jira_password))

    def getIssue(self, issue_id: str) -> Issue:

        issue = self.jira_client.issue(id=issue_id)
        return issue
