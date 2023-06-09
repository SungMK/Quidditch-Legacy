from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('teams/', views.teams_index, name='index'),
    path('teams/<int:team_id>/', views.teams_detail, name='detail'),
    path('players/', views.get_characters, name='players'), # API Call
    path('players/search/', views.search_players, name='search_players'), # Search Functionality
    path('teams/create/', views.TeamCreate.as_view(), name='teams_create'),
    path('teams/<int:pk>/update/', views.TeamUpdate.as_view(), name='teams_update'),
    path('teams/<int:pk>/delete/', views.TeamDelete.as_view(), name='teams_delete'),
]