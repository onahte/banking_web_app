import os
import click
from flask.cli import with_appcontext
from .. import config
from ..db import db

BASE_DIR = config.Config.BASE_DIR

@click.command(name='create-db')
@with_appcontext
def create_database():
    # set the name of the apps log folder to logs
    dbdir = os.path.join(BASE_DIR, '../database')
    # make a directory if it doesn't exist
    if not os.path.exists(dbdir):
        os.mkdir(dbdir)
    db.create_all()


@click.command(name='create-log')
@with_appcontext
def create_logs():
    # set the name of the apps log folder to logs
    logdir = os.path.join(BASE_DIR, '../logs')
    # make a directory if it doesn't exist
    if not os.path.exists(logdir):
        os.mkdir(logdir)