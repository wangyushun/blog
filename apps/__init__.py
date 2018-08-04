from flask import Flask
from flask_babelex import Babel

from apps.models import SQLAlchemy, db
from apps.blog import blog_blueprint
from apps.view import apps as apps_blueprint, error404
from apps.blog.models import Blog, Tag, Category
from apps.admin.modelview import admin
from apps.users import login_manager, user_blueprint


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('apps.settings') #读取配置文件

    #注册蓝图
    app.register_blueprint(apps_blueprint)
    app.register_blueprint(blog_blueprint, url_prefix='/blog')
    app.register_blueprint(user_blueprint, url_prefix='/user')

    #注册SQLAlchemy
    db.init_app(app)
    #admin后台
    admin.init_app(app)
    # admin后台语言
    babel = Babel(app)
    #注册login
    login_manager.init_app(app)
    #注册全局404错误处理
    app.register_error_handler(404, error404)

    return app


def import_models_files():
    from apps.users import models
    from apps.blog import models

def init_db():
    '''
    初始化数据库，创建表
    '''
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在元数据上,才能生成数据库表
    import_models_files()

    app = create_app()
    db.init_app(app)
    db.create_all(app=app)
    print('database tables create all ok')

def drop_db():
    '''
    删除所有数据库表
    '''
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在元数据上,才能生成数据库表
    import_models_files()
    
    ok = input('Are you sure to drop all database tables and data? yes or no ?:')
    if ok.strip() == 'yes':
        app = create_app()
        db.init_app(app)
        db.drop_all(app=app)
        print('Drop all database tables ok')

