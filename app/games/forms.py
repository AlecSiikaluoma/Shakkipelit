from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, TextAreaField, IntegerField

class GameForm(FlaskForm):
    white_player = StringField("Valkoisen pelaajan nimi", [validators.Length(min=2,max=100)])
    black_player = StringField("Mustan pelaajan nimi", [validators.Length(min=2,max=100)])
    result = IntegerField("Tulos (1 valkoiselle, 0 mustalle, -1 tasapeli)", [validators.Required("Syötä pelin tulos"), validators.NumberRange(min=-1,max=1)])
    opening = StringField("Aloitus", [validators.Length(min=2,max=100)])
    game_date = StringField("Pelin päivämäärä", [validators.Length(min=2,max=100)])
    game_location = StringField("Pelin sijainti", [validators.Length(min=2,max=100)])
    moves = TextAreaField("Siirrot", [validators.Required("Syötä pelin siirrot")])
 
    class Meta:
        csrf = False

class OpeningForm(FlaskForm):
    name = StringField("Aloituksen nimi", [validators.Length(min=2,max=100)])
    main_variation = StringField("Päävariaatio", [validators.Length(min=2,max=100)])
    moves = TextAreaField("Siirrot", [validators.Required("Syötä pelin siirrot")])
 
    class Meta:
        csrf = False