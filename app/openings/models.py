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

    @staticmethod
    def find_games_with_win_rates():
        stmt = text("select * from opening op" 
            " join (select o.name as name, count(case g.result when 1 then 1 else null end) as wins, count(case g.result when 0 then 1 else null end) as loss, count(case g.result when -1 then 1 else null end) as draw"
            " from game g join opening o on g.opening=o.name group by o.name)"
            " ap on op.name=ap.name;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row)

        return response