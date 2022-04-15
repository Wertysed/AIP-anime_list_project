from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

Genre_anime = db.Table('genr_anime',
                       db.Column('genr_id', db.Integer, db.ForeignKey('genres.id')),
                       db.Column('anime_id', db.Integer, db.ForeignKey('anime.id'))
                       )

Genre_manga = db.Table('genr_manga',
                       db.Column('genr_id', db.Integer, db.ForeignKey('genres.id')),
                       db.Column('manga_id', db.Integer, db.ForeignKey('manga.id'))
                       )



Tag_manga = db.Table('tag_manga',
                     db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
                     db.Column('manga_id', db.Integer, db.ForeignKey('manga.id'))
                     )



Tag_anime = db.Table('tag_anime',
                      db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
                      db.Column('anime_id', db.Integer, db.ForeignKey('anime.id'))
                      )


class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text)
    type = db.Column(db.Integer, db.ForeignKey('type.id'))
    episodes = db.Column(db.Integer)
    genres = db.relationship('Genres', secondary=Genre_anime,
                             backref=db.backref('anime_genres', lazy='subquery'))
    tags = db.relationship('Tags', secondary=Tag_anime,
                           backref=db.backref('anime_tag', lazy='subquery'))
    status = db.Column(db.Integer, db.ForeignKey('status.id'))
    ranked = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Float, nullable=False)
    sinpopus = db.Column(db.Text, nullable=False)
    alternative_titles = db.Column(db.Text, nullable=True)


class Manga(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text)
    type = db.Column(db.Integer, db.ForeignKey('type.id'))
    volumes = db.Column(db.Integer)
    chapters = db.Column(db.Integer)
    genres = db.relationship('Genres', secondary=Genre_manga,
                             backref=db.backref('manga', lazy='subquery'))
    tags = db.relationship('Tags', secondary=Tag_manga,
                           backref=db.backref('manga_1', lazy='subquery'))
    status = db.Column(db.Integer, db.ForeignKey('status.id'))
    ranked = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Float, nullable=False)
    sinpopus = db.Column(db.Text, nullable=False)
    alternative_titles = db.Column(db.Text, nullable=True)




class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40))


class Genres(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(55), nullable=False)


