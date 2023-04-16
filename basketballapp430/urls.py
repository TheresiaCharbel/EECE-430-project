from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name = 'login'),
    path('home/', views.home, name = 'home'),
    path('home/playerstats/', views.playerstats, name = 'playerstats'),
    path('home/playerstats/addplayer/', views.addPlayer, name = 'addplayer'),
    path('home/playerstats/updateplayer/<str:pk>/', views.updatePlayer, name = 'updatePlayer'),
    path('home/playerstats/deleteplayer/<str:pk>/', views.deletePlayer, name = 'delete-player'),
    path('home/playerstats/playerprofile/<str:pk>/', views.playerProfile, name = 'player-profile'),
    path('home/article/', views.article_list, name = 'article'),
    path('home/article/addarticle', views.addArticle, name = 'add-article'),
    path('home/article/updatearticle/<str:pk>/', views.updatearticle, name = 'update-article'),
    path('home/article/deletearticle/<str:pk>/', views.deletearticle, name = 'delete-article'),


]