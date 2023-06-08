
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render
from .models import Team, Player
from django.contrib.auth.decorators import login_required
import requests

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

def teams_index(request):
	teams = Team.objects.all()
	return render(request, 'teams/index.html', {'teams': teams})

def teams_detail(request, team_id):
	team = Team.objects.get(id=team_id)
	return render(request, 'teams/detail.html', {'team': team})

# API Functions:
def get_characters(request, limit=50):
    url = f'https://hp-api.onrender.com/api/characters?limit={limit}'
    response = requests.get(url).json()
    characters = response[:limit]
    return render(request, 'players.html', {'characters': characters})

# Class-based Views
class TeamCreate(LoginRequiredMixin, CreateView):
	model = Team
	fields = ['name', 'description'] # Add ,'players' later

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
	
class TeamUpdate(LoginRequiredMixin, UpdateView):
	model = Team
	fields = ['name', 'description'] # Add ,'players' later

class TeamDelete(LoginRequiredMixin, DeleteView):
	model = Team
	success_url = '/teams/'