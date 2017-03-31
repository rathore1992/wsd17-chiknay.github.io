"""myStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from StoreHome.views import home
from Users import views
from StoreHome import views as StoreViwes
from django.contrib.auth.views import logout



urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name='home'),
    url(r'^register/$', views.registerUser, name='register'),

    url(r'^activate$', views.activateAccount, name='activate'),
    url(r'^activate/(?P<activationCode>[a-zA-Z0-9\-]{36})/$', views.activateAccount, name='activate'),

    url(r'^login/$', views.NormalLogin, name='login'),
    url(r'^logout/$', logout, {'template_name':'Accounts/logged_out.html'},name='logout'),


    url(r'^accounts/', views.profile, name='Your Home'),

#for developer
    url(r'^Developer/games/$', StoreViwes.developer_games, name='dev_games'),

    url(r'^play/(?P<game_id>[0-9]+)/$', home, name='play_game'),
]
