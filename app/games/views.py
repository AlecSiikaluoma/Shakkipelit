from app import app, db
from flask import redirect, render_template, request, url_for
from app.games.models import Game
from app.games.forms import GameForm
from flask_login import login_required, current_user

@app.route("/games/new/")
@login_required
def games_form():
    return render_template("games/new.html", form = GameForm())

@app.route("/games/<game_id>/view")
def game_view(game_id):
    return render_template("games/view.html", game = Game.query.get(game_id))

@app.route("/games/<game_id>/edit", methods=["GET"])
@login_required
def game_edit_view(game_id):
    return render_template("games/edit.html", game = Game.query.get(game_id))

@app.route("/games/<game_id>/edit", methods=["PUT"])
@login_required
def game_edit(game_id):
	game = Game.query.get(game_id)
	game.whitePlayer = request.form.get("whitePlayer")
	game.blackPlayer = request.form.get("blackPlayer")
	game.game_date = request.form.get("game_date")
	game.game_location = request.form.get("game_location")
	game.result = request.form.get("result")
	game.opening = request.form.get("opening")
	game.moves = request.form.get("moves")

	db.session().commit()

	return redirect(url_for("game_view", game_id=game_id))

@app.route("/games/", methods=["POST"])
def games_create():
    form = GameForm(request.form)

    if not form.validate():
        return render_template("games/new.html", form = form)

    t = Game(form.white_player.data, form.black_player.data, form.game_date.data,
     form.game_location.data, form.result.data, form.opening.data, form.moves.data)

    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games", methods=["GET"])
def games_index():
    return render_template("games/list.html", games = Game.query.all())


@app.route("/games/search", methods=["GET"])
def find_games():
    return render_template("games/list.html", games = Game.find_games(request.args.get("query")))
