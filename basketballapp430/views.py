from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player, Article
from .forms import PlayerForm, ArticleForm, StatFilter

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': "Player"})

def login(request):
    return render(request, 'login.html')

def playerstats(request):
    form = StatFilter(request.GET)
    if form.is_valid():
        stat = form.cleaned_data['stat']
        if stat == '':
            players = Player.objects.all().order_by('name')
        elif stat:
            players = Player.objects.all().order_by('-{}'.format(stat))
        else:
            players = Player.objects.all().order_by('name')
    else:
        players = Player.objects.all().order_by('name')
    return render(request, 'playerstats.html', {'form': form, 'players': players})

def addPlayer(request):
    form = PlayerForm()
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('playerstats')


    context = {'form': form}
    return render(request, 'addplayer.html', context)

def updatePlayer(request, pk):
    player = Player.objects.get(id=pk)
    form = PlayerForm(instance = player)

    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('playerstats')



    context = {'form': form}
    return render(request, 'addplayer.html', context)

def deletePlayer(request, pk):
    player = Player.objects.get(id=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('playerstats')
    context = {'player': player}
    return render(request, 'deleteplayer.html', context)

def playerProfile(request, pk):
    player = Player.objects.get(id=pk)
    context = {'player': player}
    return render(request, 'playerprofile.html', context)

def article_list(request):
    articles_list = Article.objects.all()
    return render(request, 'article_list.html',{"articles" : articles_list})

def addArticle(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article')


    context = {'form': form}
    return render(request, 'addarticle.html', context)

def updatearticle(request, pk):
    article = Article.objects.get(id=pk)
    form = ArticleForm(instance = article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article')



    context = {'form': form}
    return render(request, 'addarticle.html', context)

def deletearticle(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article')
    context = {'article': article}
    return render(request, 'deletearticle.html', context)

