from django.contrib import admin

from movies.models import Movie, Actor


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'genre', 'year', 'country', 'oscars', 'cast')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    fields = ('name', 'genre', 'age', 'country', 'oscars')
