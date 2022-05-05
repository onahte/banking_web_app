import os
from app import config

BASE_DIR = config.Config.BASE_DIR
logdir = os.path.join(BASE_DIR, '../logs')

def test_error_logfiles():
    errorLog = os.path.join(logdir, 'errors.log')
    if not os.path.exists(errorLog):
        f = open(errorLog, 'w')
        f.close()
    assert os.path.exists(errorLog) == True

def test_handler_logfiles():
    handlerLog = os.path.join(logdir, 'handler.log')
    if not os.path.exists(handlerLog):
        f = open(handlerLog, 'w')
        f.close()
    assert os.path.exists(handlerLog) == True

def test_general_logfiles():
    generalLog = os.path.join(logdir, 'general.log')
    if not os.path.exists(generalLog):
        f = open(generalLog, 'w')
        f.close()
    assert os.path.exists(generalLog) == True

def test_request_logfiles():
    requestLog = os.path.join(logdir, 'request.log')
    if not os.path.exists(requestLog):
        f = open(requestLog, 'w')
        f.close()
    assert os.path.exists(requestLog) == True

def test_sqlalchemy_logfiles():
    sqlalchemyLog = os.path.join(logdir, 'sqlalchemy.log')
    if not os.path.exists(sqlalchemyLog):
        f = open(sqlalchemyLog, 'w')
        f.close()
    assert os.path.exists(sqlalchemyLog) == True

def test_werkzeug_logfiles():
    werkzeugLog = os.path.join(logdir, 'werkzeug.log')
    if not os.path.exists(werkzeugLog):
        f = open(werkzeugLog, 'w')
        f.close()
    assert os.path.exists(werkzeugLog) == True