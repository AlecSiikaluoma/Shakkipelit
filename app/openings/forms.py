from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, TextAreaField, IntegerField, StringField

class OpeningForm(FlaskForm):
    name = StringField("Aloituksen nimi", [validators.Required("Syötä aloituksen nimi"),validators.Length(min=2,max=100)])
    main_variation = StringField("Päävariaatio", [validators.Required("Syötä siirron Päävariaatio"),validators.Length(min=2,max=100)])
    moves = TextAreaField("Siirrot", [validators.Required("Syötä aloituksen siirrot")])
 
    class Meta:
        csrf = False