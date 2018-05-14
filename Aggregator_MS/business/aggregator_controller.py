import logging
import business.response_handling as RESP
import requests
import os
import json
from business.auth import requires_auth
from flask import request

USERS_MS = "http://" + os.environ['USERSADDRESS']
SONGS_MS = "http://" + os.environ['SONGSADDRESS']
PLAYLISTS_MS = "http://" + os.environ['PLAYLISTSADDRESS']
AUTH_MS = "http://" + os.environ['AUTHADDRESS']


def hello_world():
    return RESP.response_200(message='Aggregator_MS working!')


@requires_auth
def get_playlist_songs_info(id):
    """ Retrieves all playlist songs' information"""
    logging.debug("{aggregator_controller} BEGIN function get_playlist_songs_info()")

    if id is '':
        return RESP.response_400(message='A given parameter is empty')

    # Checks if song exists by sending a request into the Songs Microservice
    headers = {'Content-Type': 'application/json',
               'Authorization': request.headers['Authorization']}

    base_url = PLAYLISTS_MS + '/playlists/songs'
    url = '/'.join((base_url, str(id)))

    r = requests.get(url, headers=headers)
    if r.status_code == 400:
        return RESP.response_400()
    if r.status_code == 404:
        return RESP.response_404(message='Playlist not found!')
    if r.status_code == 500:
        return RESP.response_500(message='Playlists_MS is down!')

    response_data = json.loads(r.text)

    result = []
    for song in response_data:
        param = {'id': song['song_id']}
        r = requests.get(SONGS_MS + '/songs', params=param, headers=headers)
        if r.status_code == 404:
            return RESP.response_404(message='Song not found!')
        if r.status_code == 500:
            return RESP.response_500(message='Songs_MS is down!')
        result.append(json.loads(r.text))

    return RESP.response_200(message=result)