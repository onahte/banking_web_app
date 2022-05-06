import logging

from flask import Blueprint, render_template, abort, redirect, url_for, flash,current_app
from flask_login import login_user
from jinja2 import TemplateNotFound
from flask_login import current_user

from ..auth.forms import login_form, register_form, profile_form, security_form, user_edit_form
from ..db import db
from ..db.models import User, Transactions
from ..auth import auth
from ..logging_config import message_formatter


simple_pages = Blueprint('simple_pages', __name__, template_folder='templates')

@simple_pages.route('/main')
def main():
    log = logging.getLogger('general')
    if not current_user.is_authenticated:
        #Logging
        message = message_formatter()
        message += '::Attempted Login - Rerouted to main_login.html'
        log.info(message)
        return render_template('main_login.html')
    #Logging
    message = message_formatter()
    message += '::' + current_user.email + 'Log in success - Rerouted to index.html'
    log.info(message)
    return render_template('index.html')


@simple_pages.route('/', methods=['POST', 'GET'])
def index():
    log = logging.getLogger('general')
    form = login_form()
    if current_user.is_authenticated:
        #Logging
        message = message_formatter()
        message += '::' + current_user.email + 'Log in success - Rerouted to index.html'
        log.info(message)
        return render_template('index.html')
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            #Logging
            message = message_formatter()
            message += '::Attempted Login - Rerouted to main_login.html'
            log.info(message)
            return render_template('main_login.html')
        else:
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash("Welcome back!")
            #Logging
            message = message_formatter()
            message += '::' + current_user.email + 'Log in success - Rerouted to index.html'
            log.info(message)
            return render_template('index.html')
    return render_template('main_login.html')
