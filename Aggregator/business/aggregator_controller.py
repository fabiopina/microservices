import logging
import business.response_handling as RESP
import requests
import json
import jwt
import os

USERS_MS = "http://" + os.environ['USERSADDRESS']
SONGS_MS = "http://" + os.environ['SONGSADDRESS']
PLAYLISTS_MS = "http://" + os.environ['PLAYLISTSADDRESS']
AUTH_MS = "http://" + os.environ['AUTHADDRESS']


def hello_world():
    return RESP.response_200(message='Aggregator_MS working!')