'''Testin CSV file operation'''
import os
import csv

from app import db
from app.db.models import User, Song
from app import create_app, db, config

BASE_DIR = config.Config.BASE_DIR
uploaddir = os.path.join(BASE_DIR, '../uploads')
test_file = os.path.join(uploaddir, 'test.csv')


def test_upload_dir():
    '''Tests for existence of upload directory'''
    if not os.path.exists(uploaddir):
        os.mkdir(uploaddir)
    assert os.path.exists(uploaddir)


def test_upload_csv():
    '''Tests for csv file creation/existence'''
    fields = ['Amount', 'Type']
    rows = [['9191', 'CREDIT']]

    with open(test_file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    assert os.path.exists(test_file)


def test_csv_processed(application):
    '''Tests successful processing of CSV'''
    # Creates db and test user to associate w/ song db
    with application.app_context():
        db.create_all()
        user = User('test@test.com', 'testtest')
        db.session.add(user)
        list_of_transactions = []
        with open(filepath, encoding='utf-8-sig', errors='ignore', newline='') as file:
            fieldnames = ['Amount', 'Type']
            csv_file = csv.DictReader(file, fieldnames=fieldnames)
            next(csv_file)
            for row in csv_file:
                list_of_transactions.append(Transactions(row['Amount'], row['Type']))
                if not row['Amount'] == None:
                    temp_balance += float(row['Amount'])
        user.transactions = list_of_transactions
        db.session.commit()
        # Tests CSV data was successfully loaded to db
        test_transaction = Transactions.query.filter_by(Amount='9191').first()
        assert test_transaction.amount == '9191'
        # Breaks down test user and confirms db is empty
        db.session.delete(user)
        assert db.session.query(User).count() == 0
    # Removes test csv
    os.remove(test_file)
    assert os.path.exists(test_file) == False
