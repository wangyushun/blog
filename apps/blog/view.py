from flask import render_template, abort, request, current_app
from jinja2 import TemplateNotFound

from . import blog_blueprint
from .models import Blog, Category, Tag


@blog_blueprint.route('/', methods=['GET'], endpoint='blog')
def blog():
    page = request.args.get('page', 1)
    try:
        paginater = Blog.query.paginate(page=1, per_page=current_app.config['BLOG_NUM_PER_PAGE'], error_out=False)
        tags = Tag.query.all()
        categorys = Category.query.all()
        return render_template('blog.html', paginater=paginater, tags=tags, categorys=categorys)
    except TemplateNotFound:
        abort(404)

@blog_blueprint.route('/<id>')
def detail(id):
    id = get_int_from_str_or_404(id)
    blog = Blog.query.get_or_404(id)
    return render_template('detail.html', blog=blog)


def get_int_from_str_or_404(str_vlaue):
    try:
        id = int(str_vlaue)
    except ValueError:
        abort(404)

    return id