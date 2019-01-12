import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# App configuration
app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "blog-secret-key"

# Database setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "db.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

# Login configurations
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"

# Register the Blueprints
from blog.core.views import core
from blog.users.views import users
from blog.blog_posts.views import blog_posts
from blog.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)
