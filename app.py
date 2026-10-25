from flask import Flask;
from flask import render_template

app = Flask(__name__)

@app.route("/")

def home():
    message = "Test"
    guesses = []
    game_over = False

    return render_template(
    "wordle.html",
    message=message,
    guesses=guesses,
    game_over=game_over
)

# @app.route()

if __name__ == "__main__":
    app.run(debug=True);