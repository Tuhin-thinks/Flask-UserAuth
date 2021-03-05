from flask import Blueprint, render_template, Flask
from . import db, main
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', current_user=current_user)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user.name)