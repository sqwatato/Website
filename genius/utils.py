import environ
import lyricsgenius
import json
import os
environ.Env.read_env()
genius = lyricsgenius.Genius(os.environ['GENIUS_ACCESS_TOKEN'])

def get_song(title, author):
    try:
        song = genius.search_song(title,author)
        return song.lyrics.splitlines()
    except:
        return None





