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
    path('teams/<int:team_id>/assoc_player/<int:player_id>/', views.assoc_player, name='assoc_player'), # Adds Player Association
    path('teams/<int:team_id>/unassoc_player/<int:player_id>/', views.unassoc_player, name='unassoc_player'), # Removes Player Association
    path('teams/<int:team_id>/assoc_broomstick/<int:broomstick_id>/', views.assoc_broomstick, name='assoc_broomstick'), # Adds Broomstick Association
    path('teams/<int:team_id>/unassoc_broomstick/<int:broomstick_id>/', views.unassoc_broomstick, name='unassoc_broomstick'), # Removes Broomstick Association
    path('characters/', views.characters, name='characters_list'), # Instructions for adding character
    path('characters/all', views.get_all_characters, name='all_characters'), # API Call to get all Characters
    path('characters/students', views.get_all_students, name='all_students'), # API Call to get all Students
    path('characters/staff', views.get_all_staff, name='all_staff'), # API Call to get all Staff
    path('characters/houses/gryffindor', views.get_all_gryffindor, name='all_gryffindor'), # API Call to get all Gryffindor
    path('characters/houses/hufflepuff', views.get_all_hufflepuff, name='all_hufflepuff'), # API Call to get all Hufflepuff
    path('characters/houses/ravenclaw', views.get_all_ravenclaw, name='all_ravenclaw'), # API Call to get all Ravenclaw
    path('characters/houses/slytherin', views.get_all_slytherin, name='all_slytherin'), # API Call to get all Slytherin
    path('save-character/', views.save_character, name='save_character'), # Saves Player to database when form is submitted
    path('players/', views.PlayerList.as_view(), name='players_list'), # Player Index View
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name='players_detail'), # Player Detail Page
    path('players/create/', views.PlayerCreate.as_view(), name='players_create'), # Creates Player
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='players_update'), # Updates Players
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='players_delete'), # Deletes Players
    path('broomsticks/', views.BroomstickList.as_view(), name='broomsticks_list'), # Broomstick Index View
    path('broomsticks/<int:pk>/', views.BroomstickDetail.as_view(), name='broomsticks_detail'), # Broomstick Detail Page
    path('broomsticks/create/', views.BroomstickCreate.as_view(), name='broomsticks_create'), # Adds Broomstick
    path('broomsticks/<int:pk>/update/', views.BroomstickUpdate.as_view(), name='broomsticks_update'), # Updates Broomsticks
    path('broomsticks/<int:pk>/delete/', views.BroomstickDelete.as_view(), name='broomsticks_delete'), # Deletes Broomsticks
    path('accounts/signup/', views.signup, name='signup'), # Sign Up Page View
]