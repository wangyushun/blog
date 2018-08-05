from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login.mixins import UserMixin

from . import login_manager
from apps.models import db


class User(db.Model, UserMixin):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(20), unique=True)
	_password = db.Column('password', db.String(256))
	nickname = db.Column(db.String(20), nullable=True)
	email = db.Column(db.String(30), unique=True, nullable=True)
	telephone = db.Column(db.String(11), nullable=True)
	created_time = db.Column(db.DateTime, default=datetime.utcnow)
	is_superuser = db.Column(db.Boolean, default=False)
	userlogs = db.relationship('UserLog', backref='user', lazy='dynamic')

	__mapper_args__ = {
		"order_by": created_time.desc()
	}

	def __init__(self, username=None, password=None, is_superuser=False, *args, **kwargs):
		self.username = username
		self.password = password
		self.is_superuser = is_superuser
		super(User, self).__init__(*args, **kwargs)


	def __str__(self):
		return '<User:{0}>'.format(self.username)

	@property
	def password(self):
		return self._password

	@password.setter
	def password(self, pw):
		self._password = generate_password_hash(pw)

	def check_password(self, pw):
		return check_password_hash(self._password, pw)

	@classmethod
	def is_username_exists(self, username):
		try:
			user = self.query.filter_by(username=username).first()
			if not user:
				return False
		except Exception:
			pass
		return True

class UserLog(db.Model):
	__tablename__ = 'userlog'

	id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
	created_time = db.Column(db.DateTime, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	__mapper_args__ = {
		"order_by": created_time.desc()
	}

	def __str__(self):
		return '<Userlog: {0}>'.format(self.created_time)


@login_manager.user_loader
def load_user(user_id):
	try:
		user = User.query.get(user_id)
	except Exception:
		user = None
	return user

