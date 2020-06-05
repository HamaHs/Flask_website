from flask import Flask, render_template, redirect, url_for, abort
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('main')

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

@app.errorhandler(404)
def not_found(error):
    return render_template('not_found_404.html')


if __name__ == '__main__':
    app.run(debug=True)
