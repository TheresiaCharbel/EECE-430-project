from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name = 'login'),
    path('home/', views.home, name = 'home'),
    path('home/playerstats/', views.playerstats, name = 'playerstats'),
    path('home/playerstats/addplayer/', views.addPlayer, name = 'addplayer'),
    path('home/playerstats/updateplayer/<str:pk>/', views.updatePlayer, name = 'updatePlayer'),
    path('home/playerstats/deleteplayer/<str:pk>/', views.deletePlayer, name = 'delete-player'),
    path('home/playerstats/playerprofile/<str:pk>/', views.playerProfile, name = 'player-profile')
]