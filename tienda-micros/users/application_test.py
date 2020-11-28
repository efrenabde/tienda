# application_test.py
import pytest
import application

def testDefinition():
    application.create_app(db_uri="sqlite:///red.db")

