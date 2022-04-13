from flask import Flask, render_template, abort, request, redirect

app = Flask(__name__)


@app.route('/')
def homepage():  # put application's code here
    return render_template('homepage.html', title="ToDon't")

@app.route('/login')
def login():
    return render_template('login.html', title = 'login')

@app.route('/top_anime')
def top_anime():
    return render_template('top_anime.html', title = 'top anime')

@app.route('/top_manga')
def top_manga():
    return render_template('top_manga.html', title='top anime')

@app.route('/anime_search')
def anime_search():
    return render_template('anime_search.html', title='anime_search')

@app.route('/manga_search')
def manga_search():
    return render_template('manga_search.html', title='anime_search')

if __name__ == '__main__':
    app.run()
