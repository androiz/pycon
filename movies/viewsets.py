from rest_framework.viewsets import ModelViewSet

from .models import Movie, Actor
from .serializers import MovieSerializer, ActorSerializer


class MovieViewset(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = self.queryset
        year = self.request.query_params.get('year', None)
        if year is not None:
            queryset = queryset.filter(year=year)
        return queryset


class ActorViewset(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
