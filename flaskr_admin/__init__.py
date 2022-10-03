from flask import Flask
from flask_admin import Admin

app = Flask(__name__)


def create_app():
    # set optional bootswatch theme
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    admin = Admin(app, name='microblog', template_mode='bootstrap5')
    # Add administrative views here

    return app
