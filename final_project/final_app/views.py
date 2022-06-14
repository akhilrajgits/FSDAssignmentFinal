from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def wordle(request):
    return render(request, "wordle.html")

def tictactoe(request):
    return render(request, "tictac.html")