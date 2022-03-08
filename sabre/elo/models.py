
# Create your models here.
import math

from django.db import models
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


class Player(models.Model):
    name = models.CharField(max_length=100)
    elo_rating = models.FloatField(default=settings.ELO_START_VALUE)

    def probability(self, opponent):
        return 1 / (1 + math.pow(10, (opponent.elo_rating - self.elo_rating) / 400))

    def updated_elo(self, opponent, result):
        return self.elo_rating + settings.ELO_FACTOR_K * (result - self.probability(opponent))


class EloRated(models.Model):
    elo_rating = models.FloatField(default=settings.ELO_START_VALUE)

    class Meta:
        abstract = True

    def probability(self, opponent):
        return 1 / (1 + math.pow(10, (opponent.elo_rating - self.elo_rating) / 400))

    def updated_elo(self, opponent, result):
        
        return self.elo_rating + settings.ELO_FACTOR_K * (result - self.probability(opponent))

# def registration():
#     username = request.POST['username']
#     password = request.POST['password']
#     email = request.POST['email']
#     return HttpResponseRedirect(reverse('index'))

# def login():
#     username = request.POST['username']
#     password = request.POST['password']
#     return HttpResponseRedirect(reverse('index'))

# def logout():
#     return HttpResponseRedirect(reverse('index'))

#broken code 