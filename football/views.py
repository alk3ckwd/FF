from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse
from django.core import serializers
import json

from .models import stats, games

# Create your views here.
def index(request):
	teams = stats.objects.all()
	game = games.objects.all()
	context = {'teams': teams, 'games': games}
	return render(request, 'football/index.html', context)

def team_detail(request, pk):
	team = stats.objects.get(pk=pk)
	return render(request, 'football/team_detail.html', {'team': team})

def matchup(request):
	if request.method == 'GET':
		matchupid = request.GET.get('game_select')
		home_id = games.objects.get(pk=matchupid).home_team_id
		home_stats = stats.objects.get(pk=home_id).as_dict()
		away_id = games.objects.get(pk=matchupid).away_team_id
		away_stats = stats.objects.get(pk=away_id).as_dict()
		stats_to_return = {'home': home_stats, 'away': away_stats}
		return HttpResponse(json.dumps(stats_to_return), content_type="application/json")

def get_games(request):
	if request.method == 'GET':
		week = request.GET.get('week_select')
		game = games.objects.filter(week=week).values('id', 'away_team_id', 'home_team_id')
		final = []
		for i in range(len(game)):
			new = {'id': game[i]['id'], 'home_team': stats.objects.get(pk=game[i]['home_team_id']).team_name,
				   'away_team': stats.objects.get(pk=game[i]['away_team_id']).team_name}
			final.append(new)
		return HttpResponse(json.dumps(final), content_type="application/json")

