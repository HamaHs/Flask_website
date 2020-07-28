from flask import render_template
from project import app, db


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def db_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
