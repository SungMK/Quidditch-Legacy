from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .models import Team, Player, Broomstick
from django.contrib.auth.decorators import login_required
import requests

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

def signup(request):
    # POST request
    error_message = ''
        # user is signing up with a form submission
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/teams/create')
        else:
            error_message = 'Invalid Signup - Try Again'
    # GET request
        # user is navigating to signup page to fill out form
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error': error_message
    })

@login_required
def teams_index(request):
	teams = Team.objects.filter(user=request.user)
	return render(request, 'teams/index.html', {'teams': teams})

@login_required
def teams_detail(request, team_id):
    team = Team.objects.get(id=team_id)
    id_list = team.players.all().values_list('id', flat=True)
    players_team_doesnt_have = Player.objects.exclude(id__in=id_list)

    broomstick_list = team.broomsticks.all().values_list('id', flat=True)
    broomsticks_team_doesnt_have = Broomstick.objects.exclude(id__in=broomstick_list)
    return render(request, 'teams/detail.html', {'team': team, 'players': players_team_doesnt_have, 'broomsticks': broomsticks_team_doesnt_have})

@login_required
def assoc_player(request, team_id, player_id):
    Team.objects.get(id=team_id).players.add(player_id)
    return redirect('detail', team_id=team_id)

@login_required
def unassoc_player(request, team_id, player_id):
    Team.objects.get(id=team_id).players.remove(player_id)
    return redirect('detail', team_id=team_id)

@login_required
def assoc_broomstick(request, team_id, broomstick_id):
    Team.objects.get(id=team_id).broomsticks.add(broomstick_id)
    return redirect('detail', team_id=team_id)

@login_required
def unassoc_broomstick(request, team_id, broomstick_id):
    Team.objects.get(id=team_id).broomsticks.remove(broomstick_id)
    return redirect('detail', team_id=team_id)

# API Functions:

# With Limit
# @login_required
# def get_characters(request, limit=500):
#     url = f'https://hp-api.onrender.com/api/characters?limit={limit}'
#     response = requests.get(url).json()
#     characters = response[:limit]
#     return render(request, 'main_app/players.html', {'characters': characters})

# Without Limit
def get_characters(request):
    url = 'https://hp-api.onrender.com/api/characters'
    response = requests.get(url).json()
    characters = response
    return render(request, 'main_app/characters_list.html', {'characters': characters})

# Class-based Views:

# Team Functions:
class TeamCreate(LoginRequiredMixin, CreateView):
	model = Team
	fields = ['name', 'description']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
	
class TeamUpdate(LoginRequiredMixin, UpdateView):
	model = Team
	fields = ['name', 'description']

class TeamDelete(LoginRequiredMixin, DeleteView):
	model = Team
	success_url = '/teams/'

# Player Functions:
class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    fields = ['name', 'species', 'gender', 'house']       

class PlayerList(LoginRequiredMixin, ListView):
    model = Player

class PlayerDetail(LoginRequiredMixin, DetailView):
    model = Player

class PlayerUpdate(LoginRequiredMixin, UpdateView):
    model = Player
    fields = ['name', 'species', 'gender', 'house']   

class PlayerDelete(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = '/players/'

# Broomstick Functions:

class BroomstickCreate(LoginRequiredMixin, CreateView):
    model = Broomstick
    fields = ['choice']

class BroomstickList(LoginRequiredMixin, ListView):
    model = Broomstick

class BroomstickDetail(LoginRequiredMixin, DetailView):
    model = Broomstick

class BroomstickUpdate(LoginRequiredMixin, UpdateView):
    model = Broomstick
    fields = ['choice']

class BroomstickDelete(LoginRequiredMixin, DeleteView):
    model = Broomstick
    success_url = '/broomsticks/'