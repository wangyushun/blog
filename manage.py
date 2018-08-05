import sys

from apps import create_app, init_db, drop_db, db
from apps.users.models import User

def runserver():
    create_app().run()#host='0.0.0.0'


def list_cmds():
    print('Commands:\n')
    for cmd_name,cmd  in cmds.items():
        print('* {0:20} # {1}'.format(cmd_name, cmd[-1]))

def create_superuser():
    app = create_app()
    with app.app_context(): #app上下文入栈，不然数据库操作无法获取app
        username = input('please input username:').strip()
        if not username:
            print('username is unvalid')
            return
        if User.is_username_exists(username=username):
            print('username is exists,please use another one')
            return
        password = input('please input password:').strip()
        password2 = input('please input password again:').strip()
        if password and password == password2:
            try:
                user = User(username=username, password=password, is_superuser=True)
                db.session.add(user)
                db.session.commit()
            except Exception:
                print('create superuser error')
                return
            print('create superuser success')
        else:
            print('failed password')


def main():
    params = sys.argv
    cmd = 'runserver' if len(params) < 2 else params[1].strip()
    try:
        cmd_fun_info = cmds.get(cmd)
    except KeyError:
        print('Command is unvalid')
    cmd_fun_info[0]()


if __name__ == '__main__':
    cmds = {
        'runserver': (runserver,'Start flask server'),
        'migrate': (init_db, 'Migrate database tables of models you defined'),
        'drop_db': (drop_db, 'drop all database tables'),
        'help': (list_cmds, 'List all command'),
        'create_superuser': (create_superuser, 'Create superuser'),
    }
    main()

