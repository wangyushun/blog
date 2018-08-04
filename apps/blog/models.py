from datetime import datetime

from apps.models import db


class Category(db.Model):
	__tablename__ = 'category'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(20))
	blogs = db.relationship('Blog', backref='category', lazy=True)

	def __str__(self):
		return self.name


class Tag(db.Model):
	__tablename__ = 'tag'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(20))

	def __str__(self):
		return self.name


tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('blog_id', db.Integer, db.ForeignKey('blog.id'), primary_key=True)
)


class Blog(db.Model):
	__tablename__ = 'blog'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(256))
	author = db.Column(db.String(50))
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
	tags = db.relationship('Tag', secondary=tags, lazy='subquery', backref=db.backref('blogs', lazy=True))
	content = db.Column(db.Text())
	created_time = db.Column(db.DateTime, default=datetime.utcnow)
	modified_time = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)#utcnow不能加()，否则时间是固定的

	__mapper_args__ = {
		"order_by": created_time.desc()
	}
	def __str__(self):
		return '<Blog:{0}>'.format(self.title)






