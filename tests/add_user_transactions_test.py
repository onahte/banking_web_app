import logging

from app import db
from app.db.models import User, Transactions


def test_adding_user(application):
    with application.app_context():
        db.create_all()
        # Make sure test case is empty
        assert db.session.query(User).count() == 0
        # Build test user
        user = User('a@test.com', 'testtest', '100')
        db.session.add(user)
        # Confirm test user has been added
        assert db.session.query(User).count() == 1
        user = User.query.filter_by(email='a@test.com').first()
        # Test that the user retrieved is correct
        assert user.email == 'a@test.com'
        db.session.delete(user)
        db.session.commit()
        assert db.session.query(User).count() == 0


def test_adding_transactions(application):
    with application.app_context():
        db.create_all()
        # Confirm test case is empty
        assert db.session.query(User).count() == 0
        # Build test user
        user = User('b@test.com', 'testtest', '100')
        db.session.add(user)
        # Confirm test user has been added
        assert db.session.query(User).count() == 1
        user = User.query.filter_by(email='b@test.com').first()
        #Build test user
        user.transactions = [Transactions('9191', 'CREDIT'), Transactions('1212', 'DEBIT')]
        db.session.commit()
        # Confirm test transactions has been added
        assert db.session.query(Transactions).count() == 2
        transactions1 = Transactions.query.filter_by(amount='9191').first()
        # Test transaction 1 retrieval
        assert transactions1.amount == 9191.0
        transactions2 = Transactions.query.filter_by(amount='1212').first()
        # Test transaction 2 retrieval
        assert transactions2.amount == 1212.0
        #Test case breakdown
        db.session.delete(user)
        db.session.commit()
        assert db.session.query(User).count() == 0
        assert db.session.query(Transactions).count() == 0


def test_user_admin(application):
    with application.app_context():
        db.create_all()
        # Confirm test case is empty
        assert db.session.query(User).count() == 0
        # Build test user
        user = User('c@test.com', 'testtest', '100')
        db.session.add(user)
        db.session.commit()
        # Test user id. Only user id 1 is admin.
        assert user.id == 1
        # Test breakdown.
        db.session.delete(user)
        assert db.session.query(User).count() == 0
