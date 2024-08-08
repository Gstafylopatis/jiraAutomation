from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    env_path = basedir + ".env"

    load_dotenv(env_path)
