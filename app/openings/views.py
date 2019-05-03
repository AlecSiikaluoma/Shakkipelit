from app import app, db
from flask import redirect, render_template, request, url_for
from app.openings.models import Opening
from app.games.models import Game
from app.games.forms import GameForm
from app.openings.forms import OpeningForm
from flask_login import login_required, current_user

@app.route("/openings", methods=["GET"])
def openings_index():
    return render_template("games/listopenings.html", openings = Opening.query.all())


@app.route("/openings/", methods=["POST"])
@login_required
def openings_create():
    form = OpeningForm(request.form)

    if not form.validate():
        return render_template("games/add_opening.html", form = form)

    opening = Opening(form.name.data, form.main_variation.data, form.moves.data)

    db.session().add(opening)
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/openings/new/")
@login_required
def openings_form():
    return render_template("games/add_opening.html", form = OpeningForm())

@app.route("/opening/games", methods=["GET"])
def openings_games():
    return render_template("games/list.html", games=Opening.find_games(request.args.get("name")))