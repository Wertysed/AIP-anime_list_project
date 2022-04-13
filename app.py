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

@app.route('/ranobe_search')
def ranobe_search():
    return render_template('ranobe_search.html', title='anime_search')

@app.route('/top_ranobe')
def top_ranobe():
    return render_template('top_ranobe.html', title='top anime')

@app.route('/anime_page')
def anime_page():
    return render_template('anime_page.html', title='top anime')

@app.route('/manga_page')
def manga_page():
    return render_template('manga_and_ranobe.html', title='top anime')

@app.route('/ranobe_page')
def ranobe_page():
    return render_template('manga_and_ranobe.html', title='top anime')

@app.route('/profile')
def profile_page():
    return render_template('profile_page.html', title='top anime')

@app.route('/anime_list')
def anime_list():
    return render_template('anime_list.html', title='top anime')

@app.route('/manga_list')
def manga_list():
    return render_template('manga_list.html', title='top anime')

@app.route('/ranobe_list')
def ranobe_list():
    return render_template('ranobe_list.html', title='top anime')


if __name__ == '__main__':
    app.run()
