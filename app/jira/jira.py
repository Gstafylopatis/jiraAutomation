
from jira import JIRA

class Jira(object):

    def __init__(self, jira_server, jira_username, jira_password):
        self.jira_server = jira_server
        self.jira_username = jira_username
        self.jira_password = jira_password



        self.jira_client = JIRA(server=jira_server, basic_auth=(jira_username, jira_password))


