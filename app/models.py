from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    secure_password = db.Column(db.String(255), nullable=False)
    profile_pic_path = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password, password)

    def ___repr__():
        return f"User ('{self.username}', '{self.email}'')"


class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='blog_id', lazy="dynamic")
    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def ___repr__():
        return f"Blog ('{self.title}', '{self.date_posted}'')"


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(1000))
    name = db.Column(db.String)
    blog = db.Column(db.Integer, db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, blog):
        comments = Comment.query.filter_by(blog_id=blog).all()
        return comments

    @classmethod
    def delete_comment(cls, id):
        comment = Comment.query.filter_by(id=id).first()
        db.session.delete(comment)
        db.session.commit()

    def __repr__(self):
        return f'Comment{self.comment}'


class Quote:
    '''
    quote class to define quote object
    '''

    def __init__(self, quote, author):
        self.quote = quote
        self.author = author
