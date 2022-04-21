from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask_login import current_user
from ..auth.forms import login_form, register_form, profile_form, security_form, user_edit_form
from ..db import db
from ..db.models import User
from ..auth import auth

simple_pages = Blueprint('simple_pages', __name__,
                        template_folder='templates')

@simple_pages.route('/about')
def about():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/', methods=['POST', 'GET'])
def index():
    form = login_form()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        else:
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash("Welcome", 'success')
            return redirect(url_for('auth.dashboard'))
    return render_template('main_login.html', form=form)

# @simple_pages.route('/')
# def index():
#     try:
#         if current_user.is_authenticated:
#             return render_template('index.html')
#         return render_template('main_login.html')
#     except TemplateNotFound:
#         abort(404)