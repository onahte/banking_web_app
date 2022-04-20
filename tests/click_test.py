"""Tests creation of log dir"""
import os

from app import create_log_folder, create_database
from click.testing import CliRunner

runner = CliRunner()
root = os.path.dirname(os.path.abspath(__file__))

def test_create_log():
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    logdir = os.path.join(root, '../app/logs')
    response = os.path.exists(logdir)
    assert response == True

def test_create_database():
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    dbdir = os.path.join(root, '../database')
    response =  os.path.exists(dbdir)
    assert response == True
