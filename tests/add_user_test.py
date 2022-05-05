import logging

from app import db
from app.db.models import User, Song


def test_adding_user(application):
    log = logging.getLogger('general')
    with application.app_context():
        db.create_all()
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        # showing how to add a record
        # create a record
        user = User('test@test.com', 'testtest')
        # add it to get ready to be committed
        db.session.add(user)
        # call the commit
        # db.session.commit()
        # assert that we now have a new user
        assert db.session.query(User).count() == 1
        # finding one user record by email
        user = User.query.filter_by(email='test@test.com').first()
        log.info(user)
        # asserting that the user retrieved is correct
        assert user.email == 'test@test.com'
        # this is how you get a related record ready for insert
        user.transactions = [Transactions('9191', 'CREDIT'), Transactions('1212', 'DEBIT')]
        # commit is what saves the songs
        db.session.commit()
        assert db.session.query(Transactions).count() == 2
        transactions1 = Transactions.query.filter_by(amount='9191').first()
        assert transactions1.amount == '9191'
        transactions2 = Transactions.query.filter_by(amount='1212').first()
        assert song2.title == '1212'
        # checking cascade delete
        db.session.delete(user)
        db.session.commit()
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0


def test_user_admin(application):
    with application.app_context():
        # new record
        db.create_all()
        assert db.session.query(User).count() == 0
        user = User('test@test.com', 'testtest')
        db.session.add(user)
        db.session.commit()
        assert user.id == 1
        db.session.delete(user)
        assert db.session.query(User).count() == 0
