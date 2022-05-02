import os
import logging

from flask import Blueprint, cli
from flask_sqlalchemy import SQLAlchemy
from app import config


db = SQLAlchemy()

database = Blueprint('database', __name__, )
root = config.Config.BASE_DIR


@database.cli.command('create')
def init_db():
    db.create_all()


@database.before_app_first_request
def create_db_dir():
    dbdir = os.path.join(root, '..', config.Config.DB_DIR)
    if not os.path.exists(dbdir):
        os.mkdir(dbdir)
    db.create_all()


@database.before_app_first_request
def create_upload_csv_dir():
    uploaddir = os.path.join(root, '..', config.Config.UPLOAD_FOLDER)
    if not os.path.exists(uploaddir):
        os.mkdir(uploaddir)
    db.create_all()

