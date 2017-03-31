from msilib.schema import ListView
from django.http import HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from GameShop import models as shopmodels

def home(request):
	template = loader.get_template('home.html')
	return HttpResponse(template.render(request))


def games_list(request):
	template = loader.get_template('games_list.html')
	games = shopmodels.Game.objects.all()
	return HttpResponse(template.render(games, request))


def play_game(request, game_id):
	template = loader.get_template('play_game')
	game = Game.objects.get(pk=game_id)
	return HttpResponse(template.render(game, request))

def highscores():
	return HttpResponse()

def add_game():
	return HttpResponse()

def edit_game():
	return HttpResponse()

def sales_statistics():
	return HttpResponse()

def delete_game():
	return HttpResponse()

def login():
	return HttpResponse()

def loginpost():
	return HttpResponse()

def register():
	return HttpResponse()

def registerpost():
	return HttpResponse()

def logout():
	return HttpResponse()