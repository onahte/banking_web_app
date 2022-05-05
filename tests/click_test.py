"""Tests creation of log dir"""
import os

from app import create_logs, create_database
from click.testing import CliRunner

runner = CliRunner()
root = os.path.dirname(os.path.abspath(__file__))

def test_create_logs():
    response = runner.invoke(create_logs)
    assert response.exit_code == 0
    logdir = os.path.join(root, '../logs')
    response = os.path.exists(logdir)
    assert response == True

def test_create_database():
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    dbdir = os.path.join(root, '../database')
    response =  os.path.exists(dbdir)
    assert response == True
