from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("wordle/", views.wordle, name="wordle"),
    path("tictactoe/", views.tictactoe, name="tictactoe"),
]