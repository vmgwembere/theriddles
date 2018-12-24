import json
import os

from flask import (
    Flask, session, render_template, flash, request, redirect, url_for)

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "not a secret")

MAX_ATTEMPTS = 3
with open("data/riddles.json") as riddle_file:
    RIDDLES = json.load(riddle_file)

high_score = {
    "name": "nobody",
    "score": 0
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new_game", methods=["POST"])
def new_game():
    session["player"] = request.form["player"]
    session["score"] = 0
    session["riddle_num"] = 0
    session["riddle_attempts"] = MAX_ATTEMPTS
    return redirect(url_for("riddle"))


@app.route("/riddle", methods=["GET", "POST"])
def riddle():
    if "player" not in session:
        return redirect(url_for("index"))

    if request.method == "POST" and session["riddle_num"] < len(RIDDLES):
        previous_riddle = RIDDLES[session["riddle_num"]]
        if request.form["answer"].lower() == previous_riddle["answer"]:
            session["riddle_num"] += 1
            session["score"] += 1
            if session["riddle_num"] < len(RIDDLES):
                flash("Correct answer, %s! Your score is %s." % (
                      session["player"], session["score"]))
            else:
                flash("Correct answer, %s!" % session["player"])
        elif not session["riddle_attempts"]:
            session["riddle_num"] += 1
            session["riddle_attempts"] = MAX_ATTEMPTS
            if session["riddle_num"] < len(RIDDLES):
                flash("Wrong answer, %s. Better luck with this riddle:" % (
                      session["player"]))
        else:
            session["riddle_attempts"] -= 1
            flash("Wrong answer, %s. You have %s attempts left." % (
                  session["player"], session["riddle_attempts"]))

    if session["riddle_num"] >= len(RIDDLES):
        if session["score"] >= high_score["score"]:
            high_score["score"] = session["score"]
            high_score["name"] = session["player"]
        return render_template("game_over.html", player=session["player"],
                               score=session["score"],
                               highscore=high_score["score"],
                               highscorer=high_score["name"])

    new_riddle = RIDDLES[session["riddle_num"]]
    return render_template(
        "riddle.html", player=session["player"],
        question=new_riddle["question"], riddle_num=session["riddle_num"])
        
  

if __name__ == "__main__":
    app.run(os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "8080")),
            debug=True)