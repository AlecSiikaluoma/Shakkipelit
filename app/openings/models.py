from app import db
from sqlalchemy.sql import text

class Opening(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    main_variation = db.Column(db.String(144), nullable=False)
    moves = db.Column(db.String(144), nullable=False)

    def __init__(self, name, main_variation, moves):
        self.name = name
        self.main_variation = main_variation
        self.moves = moves

    @staticmethod    
    def find_games(name):
        stmt = text("SELECT * FROM Opening"
                    " LEFT JOIN Game ON Game.opening LIKE Opening.name"
                    " WHERE opening LIKE \"%{0}%\";".format(name))
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row)

        return response