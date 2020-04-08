from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

# On this part we binding SQLAlchemy and Marshmallow into our flask application.
db = SQLAlchemy(app)
ma = Marshmallow(app)

from project.persons.routes import persons_blueprint
app.register_blueprint(persons_blueprint, url_prefix='/persons')

from project.musics.routes import musics_blueprint
app.register_blueprint(musics_blueprint, url_prefix='/musics')
