import sys

from apps import create_app, init_db, drop_db
from flask import render_template

def runserver():
    create_app().run()#host='0.0.0.0'


def list_cmds():
    print('Commands:\n')
    for cmd_name,cmd  in cmds.items():
        print('* {0:20} # {1}'.format(cmd_name, cmd[-1]))


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
        'drop-db': (drop_db, 'drop all database tables'),
        'help': (list_cmds, 'List all command'),
    }
    main()

