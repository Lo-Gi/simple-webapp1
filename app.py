from flask import Flask, render_template
from games.snake import SnakeGame
from games.hangman import HangmanGame
from games.mastermind import MastermindGame

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/games/snake.py')
def play_snake():
    # Instantiate and use SnakeGame logic here
    snake_game = SnakeGame()
    return render_template('snake.html', game=snake_game)

@app.route('/hangman')
def play_hangman():
    # Instantiate and use HangmanGame logic here
    hangman_game = HangmanGame()
    return render_template('hangman.html', game=hangman_game)

@app.route('/mastermind')
def play_mastermind():
    # Instantiate and use MastermindGame logic here
    mastermind_game = MastermindGame()
    return render_template('mastermind.html', game=mastermind_game)