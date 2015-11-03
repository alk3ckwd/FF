from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.team_detail, name='team_detail'),
	url(r'^matchup', views.matchup, name="matchup"),
	url(r'^get_games', views.get_games, name="get_games"),
]