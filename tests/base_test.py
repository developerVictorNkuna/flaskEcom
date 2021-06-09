from unittest import TestCase
import os
from market import app
from market import db


class BaseTest(TestCase):
    def setup (self):
        #make sure that the database exist

        app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL")
