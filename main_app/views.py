from django.shortcuts import render

teams = [
	{'name': 'team1', 'description': 'hogwarts'},
	{'name': 'team2', 'description': 'UK'},
	{'name': 'team3', 'description': 'Germany'},
	{'name': 'team4', 'description': 'Japan'},
	{'name': 'team5', 'description': 'Australia'},
]

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

def team_index(request):
	return render(request, 'teams/index.html', {'teams': teams})