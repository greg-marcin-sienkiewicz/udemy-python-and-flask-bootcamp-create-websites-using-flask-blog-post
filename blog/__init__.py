from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# Register the Blueprints
from blog.core.views import core
app.register_blueprint(core)
