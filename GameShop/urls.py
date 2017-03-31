from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home),
	# For players
    url(r'^games$', views.games_list),
    url(r'^games/([0-9]{4})//$', views.play_game),
    url(r'^games/scores/([0-9]{4})/$', views.highscores),
	# For developers
	url(r'^games/add$', views.add_game),
	url(r'^games/edit/([0-9]{4})/', views.edit_game),
	url(r'^games/delete/([0-9]{4})/', views.delete_game),
	url(r'^games/statistics/([0-9]{4})/$', views.sales_statistics),
	# Get login page
	url(r'^login/$', views.login),
	# Post login
	url(r'^loginpost/$', views.loginpost),
	# Get register page
	url(r'^register/$', views.register),
	# Post registration
	url(r'^registerpost/$', views.registerpost),
	# Post only
	url(r'^logout/$', views.logout),
	]