from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Player, Article
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import PlayerForm, ArticleForm, StatFilter

# Create your views here.


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {'name': request.user})

def loginView(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Incorrect username or password")

    context = {'page': page}
    return render(request, 'login.html', context)

def registerView(request):
    form = UserCreationForm()   

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Error during registration")


    context = {'form': form}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def logoutView(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
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

@login_required(login_url='login')
def addPlayer(request):
    form = PlayerForm()
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('playerstats')


    context = {'form': form}
    return render(request, 'addplayer.html', context)


@login_required(login_url='login')
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

@login_required(login_url='login')
def deletePlayer(request, pk):
    player = Player.objects.get(id=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('playerstats')
    context = {'player': player}
    return render(request, 'deleteplayer.html', context)

@login_required(login_url='login')
def playerProfile(request, pk):
    player = Player.objects.get(id=pk)
    context = {'player': player}
    return render(request, 'playerprofile.html', context)

@login_required(login_url='login')
def article_list(request):
    articles_list = Article.objects.all()
    return render(request, 'article_list.html',{"articles" : articles_list})

@login_required(login_url='login')
def addArticle(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article')


    context = {'form': form}
    return render(request, 'addarticle.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def deletearticle(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article')
    context = {'article': article}
    return render(request, 'deletearticle.html', context) 

