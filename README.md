## 简介
一个用Flask框架构建的博客项目
## 使用
### 虚拟环境搭建
```
pip install pipenv
pipenv install	#构建虚拟环境
pipenv shell 	#激活虚拟环境
```
### 数据库
根据自己的数据库修改apps/settings.py中SQLALCHEMY_DATABASE_URI变量，以sqlite为例
```
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite' #settings
python manage.py help  		#列出可用命令参数
python manage.py migrate  	#迁移数据库
```
### 启动服务器
```
python manage.py runserver 	#启动服务器
```




