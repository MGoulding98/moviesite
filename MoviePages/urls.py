from django.urls import path
from .views import indexPageView, displayMoviesPageView, searchMoviePageView
from .views import addMoviePageView, updateMoviePageView, deleteMoviePageView, showSingleMoviePageView, showSearchedMoviePageView
urlpatterns = [
    path("displayMovies/", displayMoviesPageView, name="displayMovies"),
    path("addMovie/", addMoviePageView, name="addMovie"),
    path("updateMovie/<str:movie>/", updateMoviePageView, name="updateMovie"),
    path("deleteMovie/<str:movie>/", deleteMoviePageView, name="deleteMovie"),
    path("showSingleMovie/<str:movie>/", showSingleMoviePageView , name="showSingleMovie"),
    path("showSearchedMovie/", showSearchedMoviePageView , name="showSearchedMovie"),
    path("searchMovie/", searchMoviePageView, name="searchMovie"),
    path("", indexPageView, name="index"),
]