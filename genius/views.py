from django.shortcuts import render
from django.http import JsonResponse
import lyricsgenius
import os
from .utils import get_song

genius = lyricsgenius.Genius(os.environ['GENIUS_ACCESS_TOKEN'])
# Create your views here.

def lyrics(request, title="", author=""):
    if title == "" and author == "":
        return JsonResponse({})
    response = get_song(title, author)
    if response == None:
        return JsonResponse({
            "status": 400,
            "error": "Couldn't find lyrics"
        })
    else:
        return JsonResponse({
            "status": 200,
            "lyrics": response
        })
    