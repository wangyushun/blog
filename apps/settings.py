'''
数据库配置
MySQL   mysql+driver://username:password@hostname:port/database
Postgres    postgresql+driver://username:password@hostname:port/database
SQLite (Unix)   sqlite:////absolute/path/to/database
SQLite (Windows)    sqlite:///c:/absolute/path/to/database
'''
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:wangyushun@localhost:5432/blog'
SQLALCHEMY_TRACK_MODIFICATIONS = True

#是否开启调试模式
DEBUG = True

SECRET_KEY = 'b*ywn5ensst=q7-3d8x*u9bpy**dex*)*=gfaad1nxx0vx85%u'

#flask-admin语言设置
BABEL_DEFAULT_LOCALE = 'zh_CN'

#wtf表单csrf验证开启或关闭
WTF_CSRF_ENABLED = False

#每页显示blog数
BLOG_NUM_PER_PAGE = 10
