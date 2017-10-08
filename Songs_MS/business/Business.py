import jwt
from flask import request
from flask_jwt import jwt_required, current_identity
from database import *
import logging
import connexion


# Logging configuration
logging.basicConfig(datefmt='%d/%m/%Y %I:%M:%S', level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')


# @jwt_required()
def get_user_songs():
    print request.headers.get('Authorization')
    logging.debug('{Business} BEGIN function get_user_songs()')
    songs = CRUD.read_user_songs(1)
    logging.debug('{Business} END function get_user_songs()')
    logging.info('{Business} Songs retrieved')
    return [p.dump() for p in songs]


def get_song(song_id):
    logging.debug('{Business} BEGIN function get_song()')
    song = CRUD.read_song(song_id)
    logging.debug('{Business} END function get_song()')
    logging.info('{Business} Song retrieved')
    return song.dump()


def get_songs_criteria(title=None, artist=None):
    logging.debug('{Business} BEGIN function get_songs_criteria()')
    logging.debug('{Business} Parameters: %s, %s', title, artist)
    if title == "":
        title = None
    if artist == "":
        artist = None
    songs = CRUD.read_songs_criteria(title, artist)
    logging.debug('{Business} END function get_songs_criteria()')
    logging.info('{Business} Songs retrieved')
    return [p.dump() for p in songs]


def put_song(title=None, artist=None, album=None, release_year=None, path_song=None, song_id=None):
    logging.debug('{Business} BEGIN function put_song()')
    if title == "":
        title = None
    if artist == "":
        artist = None
    if album == "":
        album = None
    if release_year == "":
        release_year = None
    if path_song == "":
        path_song = None

    logging.debug('{Business} Parameters: %s, %s, %s, %s, %s', song_id, title, artist, album, release_year)
    song = CRUD.read_song(song_id)
    song = CRUD.update_song(song, title, artist, album, release_year, path_song)

    logging.debug('{Business} END function put_song()')
    logging.info('{Business} Song updated')
    return song.dump()


def post_song(title, artist, album, release_year, path_song, user_id):
    logging.debug('{Business} BEGIN function post_song()')
    CRUD.create_song(title, artist, album, release_year, path_song, user_id)
    logging.debug('{Business} END function post_song()')


def del_song(song_id):
    logging.debug('{Business} BEGIN function del_song()')
    song = CRUD.read_song(song_id)
    CRUD.delete_song(song)
    logging.debug('{Business} END function del_song()')


# starting connexion
app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app

application.config['SECRET_KEY'] = 'super-secret'
app.debug = True


# starting database
CRUD.create_tables()
CRUD.connect_database()


if __name__ == '__main__':
    app.run(port=5000)
