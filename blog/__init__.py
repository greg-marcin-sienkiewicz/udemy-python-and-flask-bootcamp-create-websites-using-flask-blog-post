from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# App configuration
app.config["SECRET_KEY"] = "blog-secret-key"

# Register the Blueprints
from blog.core.views import core
from blog.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)
