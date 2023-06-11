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

@login_required
def characters(request):
    return render(request, 'api_data/characters_list.html')

def signup(request):
    # POST request
    error_message = ''
        # user is signing up with a form submission
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
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
@login_required
def get_all_characters(request):
    url = 'https://hp-api.onrender.com/api/characters'
    response = requests.get(url).json()
    characters = response
    return render(request, 'api_data/all_characters.html', {'characters': characters})

@login_required
def get_all_students(request):
    url = 'https://hp-api.onrender.com/api/characters/students'
    response = requests.get(url).json()
    characters = response
    return render(request, 'api_data/all_students.html', {'characters': characters})

@login_required
def get_all_staff(request):
    url = 'https://hp-api.onrender.com/api/characters/staff'
    response = requests.get(url).json()
    characters = response
    return render(request, 'api_data/all_staff.html', {'characters': characters})

@login_required
def get_all_gryffindor(request):
    url = 'https://hp-api.onrender.com/api/characters/house/gryffindor'
    response = requests.get(url).json()
    characters = response
    return render(request, 'api_data/all_gryffindor.html', {'characters': characters})

@login_required
def get_all_hufflepuff(request):
    url = 'https://hp-api.onrender.com/api/characters/house/hufflepuff'
    response = requests.get(url).json()
    characters = response
    return render(request, 'api_data/all_hufflepuff.html', {'characters': characters})

@login_required
def get_all_ravenclaw(request):
    url = 'https://hp-api.onrender.com/api/characters/house/ravenclaw'
    response = requests.get(url).json()
    characters = response
    return render(request, 'api_data/all_ravenclaw.html', {'characters': characters})

@login_required
def get_all_slytherin(request):
    url = 'https://hp-api.onrender.com/api/characters/house/slytherin'
    response = requests.get(url).json()
    characters = response
    return render(request, 'api_data/all_slytherin.html', {'characters': characters})

@login_required
def save_character(request):
    if request.method == 'POST':
        character_name = request.POST.get('character_name')

        # Creates a new Player instance with the character data
        player = Player(name=character_name)

        # Sets properties for Player based off form field values; sets default for booleans
        player.species = request.POST.get('character_species')
        player.gender = request.POST.get('character_gender')
        player.house = request.POST.get('character_house')
        player.wizard = request.POST.get('character_wizard', False)
        player.hogwarts_student = request.POST.get('character_hogwarts_student', False)
        player.hogwarts_staff = request.POST.get('character_hogwarts_staff', False)
        player.alive = request.POST.get('character_alive', False)

        # Saves the Player instance to the database
        player.save()

    return redirect('players_list')  # Redirects to the character list page

# Class-based Views:

# Team Functions:
class TeamCreate(LoginRequiredMixin, CreateView):
    model = Team
    fields = ['name', 'description']
    template_name = 'teams/team_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
	
class TeamUpdate(LoginRequiredMixin, UpdateView):
    model = Team
    fields = ['name', 'description']
    template_name = 'teams/team_form.html'

class TeamDelete(LoginRequiredMixin, DeleteView):
    model = Team
    success_url = '/teams/'
    template_name = 'teams/team_confirm_delete.html'

# Player Functions:
class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    fields = ['name', 'species', 'gender', 'house']
    template_name = 'players/player_form.html'  

class PlayerList(LoginRequiredMixin, ListView):
    model = Player
    template_name = 'players/player_list.html'

class PlayerDetail(LoginRequiredMixin, DetailView):
    model = Player
    template_name = 'players/player_detail.html'

class PlayerUpdate(LoginRequiredMixin, UpdateView):
    model = Player
    fields = ['name', 'species', 'gender', 'house']
    template_name = 'players/player_form.html'  

class PlayerDelete(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = '/players/'
    template_name = 'players/player_confirm_delete.html'

# Broomstick Functions:
class BroomstickCreate(LoginRequiredMixin, CreateView):
    model = Broomstick
    fields = ['choice']
    template_name = 'broomsticks/broomstick_form.html'

class BroomstickList(LoginRequiredMixin, ListView):
    model = Broomstick
    template_name = 'broomsticks/broomstick_list.html'

class BroomstickDetail(LoginRequiredMixin, DetailView):
    model = Broomstick
    template_name = 'broomsticks/broomstick_detail.html'

class BroomstickUpdate(LoginRequiredMixin, UpdateView):
    model = Broomstick
    fields = ['choice']
    template_name = 'broomsticks/broomstick_form.html'

class BroomstickDelete(LoginRequiredMixin, DeleteView):
    model = Broomstick
    success_url = '/broomsticks/'
    template_name = 'broomsticks/broomstick_confirm_delete.html'