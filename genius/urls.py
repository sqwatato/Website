from django.urls import path

from . import views

urlpatterns = [
    path("<str:title>_<str:author>", views.lyrics, name="lyrics"),
]
