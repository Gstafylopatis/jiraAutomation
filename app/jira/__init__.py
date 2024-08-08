import os
from app.jira import jira

jira_url = os.getenv("SERVER")
jira_user = os.getenv("JIRA_USERNAME")
jira_password = os.getenv("PASSWORD")


def create_jira_client():
    client = jira.Jira(jira_server=jira_url, jira_username=jira_user, jira_password=jira_password)
    return client
    #print(client.getIssue('100_000'))
