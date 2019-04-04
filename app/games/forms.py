from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, TextAreaField, IntegerField

class GameForm(FlaskForm):
    white_player = StringField("Valkoisen pelaajan nimi", [validators.Length(min=2)])
    black_player = StringField("Mustan pelaajan nimi", [validators.Length(min=2)])
    result = IntegerField("Tulos (1 valkoiselle, 0 mustalle, -1 tasapeli)", [validators.Required("Syötä pelin tulos")])
    opening = StringField("Aloitus")
    game_date = StringField("Pelin päivämäärä")
    game_location = StringField("Pelin sijainti")
    moves = TextAreaField("Siirrot", [validators.Required("Syötä pelin siirrot")])
 
    class Meta:
        csrf = False