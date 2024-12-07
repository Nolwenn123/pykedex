from django.shortcuts import render

#     # [GET] API
#     # The following are the endpoints for the API (pokemons saved in the database)
#     ('get/all', views.get_all_pokemon),
#     ('get/byteamid/<int:team_id>', views.get_pokemon_by_team_id),
#
#     # [POST] API
#     # Pokemons are saved because they are on a team
#     ('post/in_this_team/<int:team_id>', views.post_pokemon),
#
#     # [PUT] API
#     # Pokemons stats might change
#     ('put/<int:id>', views.put_pokemon),
#
#     # [DELETE] API
#     # Pokemons are deleted because they are removed from a team
#     ('delete/<int:id>', views.delete_pokemon),

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pokemon


# Request on sqlite database

@api_view(['GET'])
def get_pokemon_by_team_id(request, team_id):
    pokemons = Pokemon.objects.filter(team_id=team_id)
    return Response(pokemons.values())


@api_view(['GET'])
def get_all_pokemon(request):
    pokemons = Pokemon.objects.all()
    print(pokemons.values())
    return Response(pokemons.values())


@api_view(['POST'])
def post_pokemon(request, team_id):
    pokemon = Pokemon.objects.create(
        name=request.data['name'],
        pokeapi_id=request.data['pokeapi_id'],
        team_id=team_id,
        user_id=request.data['user_id'],
        hp=request.data['hp'],
        attack=request.data['attack'],
        defense=request.data['defense'],
        special_attack=request.data['special_attack'],
        special_defense=request.data['special_defense'],
        speed=request.data['speed'],
        sprite=request.data['sprite'],
    )
    return Response(pokemon.values())


@api_view(['PUT'])
def put_pokemon(request, id):
    pokemon = Pokemon.objects.get(id=id)
    pokemon.name = request.data['name']
    pokemon.pokeapi_id = request.data['pokeapi_id']
    pokemon.team_id = request.data['team_id']
    pokemon.user_id = request.data['user_id']
    pokemon.hp = request.data['hp']
    pokemon.attack = request.data['attack']
    pokemon.defense = request.data['defense']
    pokemon.special_attack = request.data['special_attack']
    pokemon.special_defense = request.data['special_defense']
    pokemon.speed = request.data['speed']
    pokemon.sprite = request.data['sprite']
    pokemon.save()
    return Response(pokemon.values())

@api_view(['DELETE'])
def delete_pokemon(request, id):
    pokemon = Pokemon.objects.get(id=id)
    pokemon.delete()
    return Response(pokemon.values())
