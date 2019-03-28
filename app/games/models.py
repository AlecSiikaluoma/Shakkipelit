from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    white_player = db.Column(db.String(144), nullable=False)
    black_player = db.Column(db.String(144), nullable=False)
    game_date = db.Column(db.String(144), nullable=False)

    game_location = db.Column(db.String(144), nullable=True)
    result = db.Column(db.Integer, nullable=True) # 1 for white, 0 for draw, -1 for black
    opening = db.Column(db.String(144), nullable=True)
    moves = db.Column(db.String(1000), nullable=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, white_player, black_player, game_date, game_location='', result='', opening='', moves=''):
        self.white_player = white_player
        self.black_player = black_player
        self.game_date = game_date
        self.game_location = game_location
        self.result = result
        self.opening = opening
        self.moves = moves