from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'), # Home Page View
    path('about/', views.about, name='about'), # About Page View
    path('contact/', views.contact, name='contact'), # Contact Page View
    path('teams/', views.teams_index, name='index'), # Team Index View
    path('teams/<int:team_id>/', views.teams_detail, name='detail'), # Team Detail Page
    path('teams/create/', views.TeamCreate.as_view(), name='teams_create'), # Creates Team
    path('teams/<int:pk>/update/', views.TeamUpdate.as_view(), name='teams_update'), # Updates Team
    path('teams/<int:pk>/delete/', views.TeamDelete.as_view(), name='teams_delete'), # Deletes Team
    path('teams/<int:team_id>/assoc_player/<int:player_id>/', views.assoc_player, name='assoc_player'),
    path('teams/<int:team_id>/unassoc_player/<int:player_id>/', views.unassoc_player, name='unassoc_player'),
    path('characters/', views.get_characters, name='characters_list'), # API Call to get all Characters
    path('players/', views.PlayerList.as_view(), name='players_list'),# Player Index View
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name='players_detail'), # Player Detail Page
    path('players/create/', views.PlayerCreate.as_view(), name='players_create'), # Creates Player
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='players_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='players_delete'),
    path('accounts/signup/', views.signup, name='signup'), # Sign Up Page View
]