import environ
import lyricsgenius
import json
import os
environ.Env.read_env()
genius = lyricsgenius.Genius(os.environ['GENIUS_ACCESS_TOKEN'])
genius.remove_section_headers = True

def get_song(title, author):
    try:
        song = genius.search_song(title,author)
        lyrics = song.lyrics.splitlines()
        for line in lyrics:
            if "You might also like" in line or "Embed" in line:
                lyrics[lyrics.index(line)] = line.replace("You might also like", "").replace("Embed", "")
        return lyrics
    except:
        return None





