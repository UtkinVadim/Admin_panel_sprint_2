from django.urls import path

from .views import Movies, MoviesDetailApi

urlpatterns = [
    path("movies/", Movies.as_view()),
    path("movies/<uuid:id>/", MoviesDetailApi.as_view()),
]
