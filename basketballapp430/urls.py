from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginView, name = 'login'),
    path('logout/', views.logoutView, name = 'logout'),
    path('register/', views.registerView, name = 'register'),
    path('', views.home, name = 'home'),
    path('playerstats/', views.playerstats, name = 'playerstats'),
    path('playerstats/addplayer/', views.addPlayer, name = 'addplayer'),
    path('playerstats/updateplayer/<str:pk>/', views.updatePlayer, name = 'updatePlayer'),
    path('playerstats/deleteplayer/<str:pk>/', views.deletePlayer, name = 'delete-player'),
    path('playerstats/playerprofile/<str:pk>/', views.playerProfile, name = 'player-profile'),
    path('article/', views.article_list, name = 'article'),
    path('article/addarticle', views.addArticle, name = 'add-article'),
    path('article/updatearticle/<str:pk>/', views.updatearticle, name = 'update-article'),
    path('article/deletearticle/<str:pk>/', views.deletearticle, name = 'delete-article'),


]