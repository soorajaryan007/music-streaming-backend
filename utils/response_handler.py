from flask import redirect, send_file
from config import Config

def stream_song(song_url):

    if Config.ENV == "production":
        return redirect(song_url)

    return send_file(song_url, mimetype="audio/mpeg")