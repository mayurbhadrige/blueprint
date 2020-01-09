#import os
from flask import Flask


def create_app(config=None):
    """Create and return app."""
    app = Flask(__name__)
    load_blueprints(app)
    return app


def load_blueprints():
    from blue.api.routes import mod
    from blue.site.routes import mod

    app.register_blueprint(site.routes.mod)
    app.register_blueprint(api.routes.mod, url_prefix='/api')
