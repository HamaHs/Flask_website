from flask import render_template, redirect, flash
from flask_login import current_user, login_user, logout_user

from app import app
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/main')
def main_page():
    return render_template('index.html')


@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/clothes')
def clothes():
    return render_template('clothes.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login_form():
    if current_user == User.is_authenticated:
        return redirect('/main')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        return redirect('/main')
    return render_template('login.html', title='Sign in', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/main')


@app.errorhandler(404)
def not_found():
    return render_template('not_found_404.html')


if __name__ == '__main__':
    app.run()
