from flask import render_template, redirect, flash

from app import app
from app.forms import LoginForm


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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/main')
    return render_template('login.html', title='Sign in', form=form)


@app.errorhandler(404)
def not_found(error):
    return render_template('not_found_404.html')


if __name__ == '__main__':
    app.run(debug=True)
