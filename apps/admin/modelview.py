from flask import redirect, request, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from apps.models import db
from apps.blog.models import Blog, Tag, Category
from apps.users.models import User, UserLog

admin = Admin(name='Admin', template_mode='bootstrap3')

class BaseModelView(ModelView):
    def is_accessible(self):
        '''
        权限设置
        '''
        if current_user.is_authenticated and current_user.is_superuser:
            return True
        return False

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('user_bp.login', next=request.url))


class BlogAdminView(BaseModelView):
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


class TagAdminView(BaseModelView):
    column_list = ('id', 'name')
    column_labels = {
        'id': '序号',
        'name': '标签名',
        'blogs': '关联博客'
    }
    def __init__(self, session, *args, **kwargs):
        super(TagAdminView, self).__init__(Tag, session, *args, **kwargs)


class CategoryAdminView(BaseModelView):
    column_list = ('id', 'name')
    column_labels = {
        'id': '序号',
        'name': '分类名',
        'blogs': '关联博客'
    }
    def __init__(self, session, *args, **kwargs):
        super(CategoryAdminView, self).__init__(Tag, session, *args, **kwargs)


class UserAdminView(BaseModelView):
    column_list = ('id', 'username', 'nickname', 'email', 'telephone', 'is_superuser', 'created_time')
    column_labels = {
        'id': '序号',
        'username': '用户名',
        'password': '密码',
        'email': '邮箱',
        'is_superuser': '管理员',
        'created_time': '创建时间',
        'telephone': '电话',
        'nickname': '昵称'
    }

    def __init__(self, session, *args, **kwargs):
        super(UserAdminView, self).__init__(User, session, *args, **kwargs)



# admin注册模型视图蓝图会使用endpoint命名，不指定默认使用类名，为防止蓝图名冲突，这里明确指定一下
admin.add_view(BlogAdminView(db.session, name='博客', endpoint='blog_admin'))
admin.add_view(CategoryAdminView(db.session, name='分类', endpoint='category_admin'))
admin.add_view(TagAdminView(db.session, name='标签', endpoint='tag_admin'))
admin.add_view(UserAdminView(db.session, name='用户', endpoint='user_admin'))