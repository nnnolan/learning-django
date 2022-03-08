from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def index(request):
    return render(request, 'elo/index.html')
    
def leaderboard(request, question_id):
    return HttpResponse("You're looking at question the leaderboard.")

def recent_matches(request, question_id):
    response = "You're looking at the recent matches."
    return HttpResponse(response)

def signup(request, question_id):
    return HttpResponse("You're looking at the signup.")