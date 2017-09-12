from django.db import models

# Create your models here.

GENRE = (
    ('H', 'Hombre'),
    ('M', 'Mujer'),
)


class Actor(models.Model):
    name = models.CharField(max_length=250)
    sex = models.CharField(max_length=50, choices=GENRE)
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    oscars = models.IntegerField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    year = models.IntegerField()
    country = models.CharField(max_length=50)
    oscars = models.IntegerField()

    cast = models.ManyToManyField(Actor, related_name='actors')

    def __str__(self):
        return self.title
