from rest_framework.serializers import ModelSerializer
from .models import Movie, Actor


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'genre', 'age', 'oscars')


class MovieSerializer(ModelSerializer):
    cast = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'genre', 'year', 'oscars', 'cast')
