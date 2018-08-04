from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from apps.models import db
from apps.blog.models import Blog, Tag, Category

admin = Admin(name='Admin', template_mode='bootstrap3')

class BlogAdminView(ModelView):
    # def is_accessible(self):
    #     if current_user.is_authenticated and current_user.username == "admin":
    #         return True
    #     return False
    # can_create = False

    column_list = ('id', 'title', 'author', 'category', 'tags', 'created_time')
    column_labels = {
        'id': '序号',
        'title': '标题',
        'created_time': '发布时间',
        'content': '正文',
        'modified_time': '修改时间',
        'category': '分类',
        'author': '作者',
        'tags': '标签'
    }
    def __init__(self, session, *args, **kwargs):
        super(BlogAdminView, self).__init__(Blog, session, *args, **kwargs)

admin.add_view(BlogAdminView(db.session, name='博客'))
admin.add_view(ModelView(Category, db.session, name='分类'))
admin.add_view(ModelView(Tag, db.session, name='标签'))