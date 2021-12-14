from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=50, primary_key=True, verbose_name="Movie Name")
    release_date = models.DateField(default=datetime.today, verbose_name="Release Date")
    runtime = models.IntegerField(default=0, verbose_name="Runtime in Minutes")
    dbmb_rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="DBMB Rating", validators=[MaxValueValidator(10), MinValueValidator(0)])
    genre = models.ForeignKey('Genre', models.DO_NOTHING, to_field='genre_name', verbose_name="Genre")
    
    def save(self) :
        self.movie_name = self.movie_name.title()

        super(Movie, self).save()

    def __str__(self):
        return (self.movie_name)

class Genre(models.Model):
    genre_name = models.CharField(max_length=50, primary_key=True, verbose_name="Genre Name")
    genre_description = models.CharField(max_length=250, verbose_name="Genre Description")
    
    def save(self) :
        self.genre_name = self.genre_name.title()

        super(Genre, self).save()

    def __str__(self) :
        return (self.genre_name)