from django.urls import path

from . import views
from .pokeapi import views as p_views

urlpatterns = [
    # [GET] POKEAPI
    # The following are the endpoints for the PokeAPI
    # https://pokeapi.co/docs/v2/pokemon
    path('pokeapi/get/one/<str:name>', p_views.get_pokemon_from_pokeapi_by_name),
    path('pokeapi/get/one/<int:id>', p_views.get_pokemon_from_pokeapi_by_id),
    path('pokeapi/get/some/<int:limit>/<int:offset>', p_views.get_some_pokemon_from_pokeapi),
    path('pokeapi/get/some/<str:search_letters>/<int:limit>/<int:offset>', p_views.get_some_pokemon_from_pokeapi_by_letters),
    path('pokeapi/get/all', p_views.get_all_pokemon_from_pokeapi),

    # [GET] API
    # The following are the endpoints for the API (pokemons saved in the database)
    path('get/all', views.get_all_pokemon),
    path('get/byteamid/<int:team_id>', views.get_pokemon_by_team_id),

    # [POST] API
    # Pokemons are saved because they are on a team
    path('post/in_this_team/<int:team_id>', views.post_pokemon),

    # [PUT] API
    # Pokemons stats might change
    path('put/<int:id>', views.put_pokemon),

    # [DELETE] API
    # Pokemons are deleted because they are removed from a team
    path('delete/<int:id>', views.delete_pokemon),
]
