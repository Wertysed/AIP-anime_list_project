from flask import Flask, render_template, abort, request, redirect
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
from models import db, bcrypt, Anime, Genres, Genre_anime, Status, Tags, Tag_anime, Type, Manga, Tag_manga, Genre_manga
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)
db.create_all()
bcrypt.init_app(app)

@app.route('/')
def homepage():  # put application's code here
    inf_top_anime = []
    inf_genre_top_anime = []
    inf_spring_anime = []
    inf_top_manga = []
    inf_top_not = []
    for ii in range(5):
        anime = Anime.query.filter_by(ranked=ii+1)
        for rr in anime:
            inf_top_anime.append(rr)
            genres = db.session.query(Genre_anime).filter_by(anime_id=rr.id)
            genre_anime = []
            for i, k in genres:
                genr = Genres.query.get(i)
                genre_anime.append(genr.name)
            genre_anime = ', '.join(genre_anime)
            inf_genre_top_anime.append(genre_anime)
            print(inf_genre_top_anime[ii])


    anime_spring = Anime.query.filter_by(status=2)
    for zz in anime_spring:
        inf_spring_anime.append(zz)
    print(';;;;;;',inf_spring_anime)

    anime_not = Anime.query.filter_by(status=3)
    for hh in anime_not:
        inf_top_not.append(hh)
    print(inf_top_not)

    for vv in range(3):
        manga = Manga.query.filter_by(ranked=vv+1)
        for gg in manga:
            inf_top_manga.append(gg)


    return render_template('homepage.html', title="homepage", inf_top_anime=inf_top_anime, inf_genre_top_anime= inf_genre_top_anime, inf_spring_anime=inf_spring_anime, inf_top_manga=inf_top_manga, inf_top_not=inf_top_not)


@app.route('/login')
def login():
    return render_template('login.html', title='login')


@app.route('/top_anime')
def top_anime():
    anime = Anime.query.all()
    status = Status.query.all()
    print(status)
    return render_template('top_anime.html', title='top anime', anime = anime, status=status)


@app.route('/top_manga')
def top_manga():
    manga = Manga.query.all()
    return render_template('top_manga.html', title='top manga', manga=manga)


@app.route('/anime_search')
def anime_search():
    anime = Anime.query.all()
    return render_template('anime_search.html', title='anime_search', anime=anime)


@app.route('/manga_search')
def manga_search():
    manga = Manga.query.all()
    return render_template('manga_search.html', title='manga_search', manga=manga)


@app.route('/anime_page/<int:id>', methods=['GET', 'POST'])
def anime_page(id):
    anime = Anime.query.get(id)
    type =  Type.query.get(anime.type)
    status = Status.query.get(anime.status)
    print(status.name)
    #genres = Genre_anime.select().where(Genre_anime.c.anime_id == anime.id)
    #genre = conn.execute(genres)

    genres = db.session.query(Genre_anime).filter_by(anime_id=anime.id)
    genre_anime = []
    for i, k in genres:
        genr = Genres.query.get(i)
        genre_anime.append(genr.name)
    genre_anime = ', '.join(genre_anime)

    tags = db.session.query(Tag_anime).filter_by(anime_id=anime.id)
    tag_anime = []
    for i, k in tags:
        tag = Tags.query.get(i)
        tag_anime.append(tag.name)
    tag_anime = ', '.join(tag_anime)
    return render_template('anime_page.html', anime = anime, status = status, genre_anime = genre_anime, tag_anime = tag_anime, type = type)

@app.route('/search_anime')
def search_anime():
    text = escape(request.args.get('text', ''))
    anime = Anime.query.filter(Anime.title.like(f'%{text}%')).all()

    print('ДДЖЫВЛОАШЩЗФЫРджфолыамго', text)
    print(anime)
    return render_template('anime_search.html', anime=anime)

@app.route('/search_manga')
def search_manga():
    text = escape(request.args.get('text', ''))
    manga = Manga.query.filter(Manga.title.like(f'%{text}%')).all()

    print('ДДЖЫВЛОАШЩЗФЫРджфолыамго', text)
    print(manga)
    return render_template('manga_search.html', manga=manga)


@app.route('/manga_page/<int:id>', methods=['GET', 'POST'])
def manga_page(id):
    manga = Manga.query.get(id)
    type =  Type.query.get(manga.type)
    status = Status.query.get(manga.status)
    print(status.name)
    #genres = Genre_anime.select().where(Genre_anime.c.anime_id == anime.id)
    #genre = conn.execute(genres)

    genres = db.session.query(Genre_manga).filter_by(manga_id=manga.id)
    genre_manga = []
    for i, k in genres:
        genr = Genres.query.get(i)
        genre_manga.append(genr.name)
    genre_manga = ', '.join(genre_manga)
    print(genre_manga)
    tags = db.session.query(Tag_manga).filter_by(manga_id=manga.id)
    tag_manga = []
    for i, k in tags:
        tag = Tags.query.get(i)
        tag_manga.append(tag.name)
    tag_manga = ', '.join(tag_manga)
    return render_template('manga_and_ranobe.html', manga = manga, status = status, genre_manga = genre_manga, tag_manga = tag_manga, type = type)


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
