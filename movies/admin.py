from django.contrib import admin

# Register your models here.

from .models import Movie

admin.site.register(Movie)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'audience', 'release_date', 'genre', 'score', 'poster_url', 'description')