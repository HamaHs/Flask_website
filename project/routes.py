from flask import render_template, redirect, flash, request, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import app, db
from app.forms import LoginForm, RegistrationForm, EditeProfilForm
from app.models import User


@app.route('/')
@app.route('/main')
def main_page():
    return render_template('index.html', title='Головна сторінка')

# with app.test_request_context():
#     print(url_for('main_page'))


@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/clothes')
# @login_required
def clothes():
    return render_template('clothes.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login_form():
    """перевіряє чи користувач авторизований"""
    if current_user.is_authenticated:
        return redirect('/main')

    form = LoginForm() #Екземпляр класа LoginForm(); app/forms.py/LoginForms()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        """для обробки next аргументу"""
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = '/main'
            return redirect(next_page)
        return redirect(next_page)

    return render_template('login.html', title='Sign in', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/main')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/main')
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user_name = User.query.filter_by(username=username).first_or_404()
    user_title = User.query.filter_by(username=username).first()
    title = 'Кабінет користувача - {}'.format(user_title)
    return render_template('user.html', user=user_name, title=title)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditeProfilForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        return redirect(url_for('user', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)