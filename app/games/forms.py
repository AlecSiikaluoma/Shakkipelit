from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, TextAreaField, IntegerField, StringField

class GameForm(FlaskForm):
    white_player = StringField("Valkoisen pelaajan nimi", [validators.Length(min=2,max=100)])
    black_player = StringField("Mustan pelaajan nimi", [validators.Length(min=2,max=100)])
    result = IntegerField("Tulos (1 valkoiselle, 0 mustalle, -1 tasapeli)", [validators.AnyOf([-1,0,1])], default=0)
    opening = StringField("Aloitus", [validators.Required("Syötä pelin aloitus"),validators.Length(min=2,max=100)])
    game_date = StringField("Pelin päivämäärä", [validators.Required("Syötä pelin päivämäärä"), validators.Length(min=2,max=100)])
    game_location = StringField("Pelin sijainti", [validators.Required("Syötä pelin sijainti"), validators.Length(min=2,max=100)])
    moves = TextAreaField("Siirrot", [validators.Required("Syötä pelin siirrot")])
 
    class Meta:
        csrf = False

class OpeningForm(FlaskForm):
    name = StringField("Aloituksen nimi", [validators.Required("Syötä aloituksen nimi"),validators.Length(min=2,max=100)])
    main_variation = StringField("Päävariaatio", [validators.Required("Syötä siirron Päävariaatio"),validators.Length(min=2,max=100)])
    moves = TextAreaField("Siirrot", [validators.Required("Syötä aloituksen siirrot")])
 
    class Meta:
        csrf = False