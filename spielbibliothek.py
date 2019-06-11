from flask import Flask, redirect, render_template

app = Flask(__name__)

class Game(object):
    def __init__(self, name, category, plataform):
        self.name = name
        self.category = category
        self.plataform = plataform

game_list = [
    Game('Tetris', 'Puzzle', 'Arcade'),
    Game('Super Mario', 'Plataform', 'Super Nintendo System'),
    Game('Pokemon Gold', 'RPG', 'Game Boy Color')
]

@app.route('/')
def index():
    return render_template('list.html', title='Games', games=game_list)

@app.route('/form')
def game_form():
    return render_template('form.html', title='New Game')

@app.route('/new-game')
def new_game():
    name = request.form['name']
    category = request.form['category']
    plataform = request.form['plataform']
    game = Game(name, category, plataform)
    game_list.append(game)
    return redirect('/start')

app.run(debug=True)