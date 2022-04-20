import click
import os
from flask.cli import with_appcontext
from ..db import db

root = os.path.dirname(os.path.abspath(__file__))

@click.command(name='create-db')
@with_appcontext
def create_database():
    dbdir = os.path.join(root, '../../database')
    if not os.path.exists(dbdir):
        os.mkdir(dbdir)
    db.create_all()

@click.command(name='create-log')
@with_appcontext
def create_logs():
    logdir = os.path.join(root, '../logs')
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    os.create_all()