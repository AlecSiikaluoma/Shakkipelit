
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
	app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///games.db"
	# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
	app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Luetaan kansiosta application tiedoston views sisältö
from app import views
from app.games import models
from app.games import views
from app.openings import models
from app.openings import views

from app.auth import models 
from app.auth import views

# kirjautuminen
from app.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Luodaan lopulta tarvittavat tietokantataulut
try: 
    db.create_all()
except:
    pass