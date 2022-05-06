import csv
import logging
import os

from babel.numbers import format_currency, parse_decimal
from flask import Blueprint, render_template, abort, url_for,current_app, flash
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound

from app.logging_config import message_formatter
from app.db import db
from app.db.models import Transactions
from app.transactions.forms import csv_upload
from werkzeug.utils import secure_filename, redirect

transactions = Blueprint('transactions', __name__, template_folder='templates')


@transactions.route('/transactions_browse', methods=['GET'], defaults={"page": 1})
@transactions.route('/transactions_browse/<int:page>', methods=['GET'])
def transactions_browse(page):
    page = page
    per_page = 1000
    pagination = Transactions.query.paginate(page, per_page, error_out=False)
    data = pagination.items
    try:
        return render_template('transactions_browse.html',data=data,pagination=pagination)
    except TemplateNotFound:
        abort(404)
    except OperationalError:
        flash('Database does not exist. Please upload a file.')
        return render_template('upload.html', form=form)

@transactions.route('/transactions_browse/upload', methods=['POST', 'GET'])
@login_required
def transactions_upload():
    form = csv_upload()

    if form.validate_on_submit():
        log = logging.getLogger('general')

        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        message = message_formatter()
        message += '::Uploaded:' + filename
        log.info(message)
        balance = 0.0
        temp_balance = 0.0
        if not current_user.balance == None:
            balance = float(parse_decimal(current_user.balance, locale='en_US'))
        list_of_transactions = []
        with open(filepath, encoding='utf-8-sig', errors='ignore', newline='') as file:
            fieldnames = ['Amount', 'Type']
            csv_file = csv.DictReader(file, fieldnames=fieldnames)
            next(csv_file)
            for row in csv_file:
                list_of_transactions.append(Transactions(row['Amount'],row['Type']))
                if not row['Amount'] == None:
                    temp_balance += float(row['Amount'])
        current_user.transactions = list_of_transactions
        current_user.transactions.user_id = current_user.id
        current_user.balance = str(format_currency(balance + temp_balance, 'USD', locale='en_US'))
        db.session.commit()

        return redirect(url_for('transactions.transactions_browse'))

    try:
        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)
