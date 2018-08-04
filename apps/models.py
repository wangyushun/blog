from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):

    @contextmanager
    def auto_commit(self):
        '''
        自动提交上下文管理器，with代码块数据库操作自动提交，错误回滚
        :return:
        '''
        yield
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

db = SQLAlchemy()

