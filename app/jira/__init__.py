import os

from jira import JIRA

from app.jira import jira
from flask import Blueprint

bp = Blueprint("jira", __name__)

from app.jira import routes
