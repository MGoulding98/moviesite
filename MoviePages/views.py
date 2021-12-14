from django.shortcuts import render
from django.http import HttpResponse
from MoviePages.models import Movie
from .models import Genre

# Our Views
def indexPageView(request) :
    return render(request, 'MoviePages/index.html')

def displayMoviesPageView(request) :
    data = Movie.objects.all().order_by('movie_name')

    context = { 
        "record" : data
    }

    return render(request, 'MoviePages/displayMovies.html', context)

def showSingleMoviePageView(request, movie) :
    data = Movie.objects.filter(movie_name = movie)

    context = { 
        "record" : data
    }
    return render(request, 'MoviePages/showSingleMovie.html', context)

def showSearchedMoviePageView(request) :
    movie = request.POST['movie_name']


    data = Movie.objects.filter(movie_name = movie)

    context = { 
        "record" : data
    }
    return render(request, 'MoviePages/showSingleMovie.html', context)

def addMoviePageView(request):
    if request.method == 'POST' :
        genre = Genre.objects.get(genre_name = request.POST['genre'])

        movie = Movie()
        movie.movie_name = request.POST['movie_name']
        movie.release_date = request.POST['release_date']
        movie.runtime = request.POST['runtime']
        movie.dbmb_rating = request.POST['dbmb_rating']
        movie.genre = genre

        movie.save()

        return render(request, 'MoviePages/index.html')
    else : 
        genres = Genre.objects.all()

        context = {
            "genres" : genres
        }
        return render(request, 'MoviePages/addMovie.html', context)

def updateMoviePageView(request, movie):
   
    if request.method == 'POST' :

        genre = Genre.objects.get(genre_name = request.POST['genre'])
        movie = Movie.objects.get(movie_name = movie)

        movie.movie_name = request.POST['movie_name']
        movie.release_date = request.POST['release_date']
        movie.runtime = request.POST['runtime']
        movie.dbmb_rating = request.POST['dbmb_rating']
        movie.genre = genre

        movie.save()

        return render(request, 'MoviePages/index.html')
    else :
      
        data = Movie.objects.filter(movie_name = movie)
        genres = Genre.objects.all()

        context = {
            "record" : data[0],
            "genres" : genres
        }

        return render(request, 'MoviePages/updateMovie.html', context)
    
def deleteMoviePageView(request, movie):
    data = Movie.objects.filter(movie_name = movie)

    data.delete()

    return displayMoviesPageView(request)


def searchMoviePageView(request) : 
    genres = Genre.objects.all()

    context = {
        "genres" : genres
    }

    return render(request, 'MoviePages/searchMovie.html', context)