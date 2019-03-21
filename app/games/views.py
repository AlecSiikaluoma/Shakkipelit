from app import app, db
from flask import redirect, render_template, request, url_for
from app.games.models import Game

@app.route("/games/new/")
def games_form():
    return render_template("games/new.html")

@app.route("/games/<game_id>/view")
def game_view(game_id):
    return render_template("games/view.html", game = Game.query.get(game_id))

@app.route("/games/<game_id>/edit", methods=["GET"])
def game_edit_view(game_id):
    return render_template("games/edit.html", game = Game.query.get(game_id))

@app.route("/games/<game_id>/edit", methods=["PUT"])
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
    t = Game(request.form.get("whitePlayer"),
     request.form.get("blackPlayer"), request.form.get("game_date"), request.form.get("game_location"),
     request.form.get("result"), request.form.get("opening"),
     request.form.get("moves"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games", methods=["GET"])
def games_index():
    return render_template("games/list.html", games = Game.query.all())


