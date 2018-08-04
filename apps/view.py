from flask import Blueprint, render_template, redirect, url_for

apps = Blueprint('apps', __name__)

@apps.route('/')
def index():
    return redirect(url_for('blog_bp.blog'))

@apps.route('/about')
def about():
    return render_template('about.html')


def error404(e):
    return render_template('404.html')
