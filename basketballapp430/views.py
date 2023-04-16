from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player
from .forms import PlayerForm

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': "Fawzi"})

def login(request):
    return render(request, 'login.html')

def playerstats(request):
    players = Player.objects.all()
    context = {"players": players}
    return render(request, 'playerstats.html', context)

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


