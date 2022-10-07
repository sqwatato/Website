from django.contrib import admin
from .models import *
# Register your models here.

class SongAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author")


admin.site.register(Song, SongAdmin)
