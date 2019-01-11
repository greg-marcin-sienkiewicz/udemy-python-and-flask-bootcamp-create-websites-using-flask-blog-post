from datetime import datetime

from blog import db, login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)


class User(db.Model, UserMixin):
  __tablename__ = "users"
  
  id = db.Column(db.Integer, primary_key=True)
  profile_image = db.Column(db.String(50), nullable=False, default="default_profile.png")
  email = db.Column(db.String(50), unique=True, index=True)
  username = db.Column(db.String(50), unique=True, index=True)
  password = db.Column(db.String(200))

  posts = db.relationship("BlogPost", backref="author", lazy=True)

  def __init__(self, email, username, password):
    self.email = email
    self.username = username
    self.password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)

  def __repr__(self):
    return f"Username {self.username}"


class BlogPost(db.Model):
  __tablename__ = "blogs"

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  title = db.Column(db.String(200), nullable=False)
  text = db.Column(db.Text, nullable=False)

  users = db.relationship(User)

  def __init__(self, title, text, user_id):
    self.title = title
    self.text = text
    self.user_id = user_id

  def __repr__(self):
    return f"Post ID: {self.id}"

