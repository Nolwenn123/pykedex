#     # The following are the endpoints for the PokeAPI
#     # https://pokeapi.co/docs/v2/pokemon
#     ('pokeapi/get/one/<str:name>', views.get_pokemon_from_pokeapi_by_name),
#     ('pokeapi/get/one/<int:id>', views.get_pokemon_from_pokeapi_by_id),
#     ('pokeapi/get/some/<int:limit>/<int:offset>', views.get_some_pokemon_from_pokeapi),
#     ('pokeapi/get/some/<str:name>', views.get_some_pokemon_from_pokeapi_by_letters),
#     ('pokeapi/get/all', views.get_all_pokemon_from_pokeapi),
#
from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response
from ..models import Pokemon


@api_view(['GET'])
def get_pokemon_from_pokeapi_by_name(request, name):
    pokeapi_url = f'https://pokeapi.co/api/v2/pokemon/{name}'

    try:
        response = requests.get(pokeapi_url)
        if response.status_code == 200:
            poke_data = response.json()

            # Fetch Pokemon species data for memo (description)
            species_response = requests.get(poke_data['species']['url'])
            species_data = species_response.json() if species_response.status_code == 200 else {}
            description = next((entry['flavor_text'] for entry in species_data.get('flavor_text_entries', []) if
                                entry['language']['name'] == 'en'), '')

            # Extract special ability
            special_ability = next(
                (ability['ability']['name'] for ability in poke_data['abilities'] if ability['is_hidden']), '')

            pokemon = {
                'order': poke_data.get('order', 0),
                'name': poke_data.get('name', ''),
                'lvl': 1,  # Assuming default level 1
                'xp': poke_data.get('base_experience', 0),
                'number': poke_data.get('id', 0),
                'type_1': poke_data['types'][0]['type']['name'] if poke_data['types'] else '',
                'type_2': poke_data['types'][1]['type']['name'] if len(poke_data['types']) > 1 else '',
                'special_capacity': special_ability,
                'memo': description,
                'atck': poke_data['stats'][1]['base_stat'] if len(poke_data['stats']) > 1 else 0,
                'defs': poke_data['stats'][2]['base_stat'] if len(poke_data['stats']) > 2 else 0,
                'atck_spe': poke_data['stats'][3]['base_stat'] if len(poke_data['stats']) > 3 else 0,
                'defs_spe': poke_data['stats'][4]['base_stat'] if len(poke_data['stats']) > 4 else 0,
                'speed': poke_data['stats'][5]['base_stat'] if len(poke_data['stats']) > 5 else 0,
                'hp': poke_data['stats'][0]['base_stat'] if poke_data['stats'] else 0,
                'team_id': 0,  # Assuming no team by default
                'shiny': False,  # You might want to set this based on some condition
                'image_url': poke_data['sprites']['front_default'],
                'shiny_image_url': poke_data['sprites']['front_shiny']
            }

            return Response(pokemon)
        else:
            return HttpResponseNotFound({'message': 'Pokemon not found or error in PokeAPI'})
    except requests.RequestException as e:
        # Log the exception
        return HttpResponseBadRequest({'message': 'Error in fetching data from PokeAPI'})


@api_view(['GET'])
def get_pokemon_from_pokeapi_by_id(request, id):
    """
    Get a pokemon from the PokeAPI by id.
    :param request: the Django HttpRequest object.
    :param id: the id of the pokemon.
    :return: JsonResponse with pokemon data or an error response.
    """
    pokeapi_url = f'https://pokeapi.co/api/v2/pokemon/{id}'

    try:
        response = requests.get(pokeapi_url)

        # Check if the response from PokeAPI is successful
        if response.status_code == 200:
            return Response(response.json())
        else:
            # If the Pokémon is not found or any other error occurs
            return HttpResponseNotFound({'message': 'Pokemon not found or error in PokeAPI'})

    except requests.RequestException as e:
        # Log the exception (you can use Django's logging mechanism)
        # log.exception("Error fetching data from PokeAPI: %s", e)
        return HttpResponseBadRequest({'message': 'Error in fetching data from PokeAPI'})


@api_view(['GET'])
def get_some_pokemon_from_pokeapi(request, limit, offset):
    """
    Get some pokemon from the PokeAPI by limit and offset.
    :param request: the Django HttpRequest object.
    :param limit: the limit of the pokemon.
    :param offset: the offset of the pokemon.
    :return: JsonResponse with pokemon data or an error response.
    """
    pokeapi_url = f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}'

    try:
        response = requests.get(pokeapi_url)

        # Check if the response from PokeAPI is successful
        if response.status_code == 200:
            return Response(response.json())
        else:
            # If the Pokémon is not found or any other error occurs
            return HttpResponseNotFound({'message': 'Pokemon not found or error in PokeAPI'})

    except requests.RequestException as e:
        # Log the exception (you can use Django's logging mechanism)
        # log.exception("Error fetching data from PokeAPI: %s", e)
        return HttpResponseBadRequest({'message': 'Error in fetching data from PokeAPI'})


@api_view(['GET'])
def get_all_pokemon_from_pokeapi(request):
    """
    Get all pokemon from the PokeAPI.
    :param request: the Django HttpRequest object.
    :return: JsonResponse with pokemon data or an error response.
    """
    pokeapi_url = f'https://pokeapi.co/api/v2/pokemon'

    try:
        response = requests.get(pokeapi_url)

        # Check if the response from PokeAPI is successful
        if response.status_code == 200:
            return Response(response.json())
        else:
            # If the Pokémon is not found or any other error occurs
            return HttpResponseNotFound({'message': 'Pokemon not found or error in PokeAPI'})

    except requests.RequestException as e:
        # Log the exception (you can use Django's logging mechanism)
        # log.exception("Error fetching data from PokeAPI: %s", e)
        return HttpResponseBadRequest({'message': 'Error in fetching data from PokeAPI'})


@api_view(['GET'])
def get_some_pokemon_from_pokeapi_by_letters(request, search_letters, limit=1, offset=0):
    pokeapi_url = 'https://pokeapi.co/api/v2/pokemon?limit=1118&offset=0'
    try:
        response = requests.get(pokeapi_url)
        if response.status_code == 200:
            all_pokemon = response.json()['results']
            filtered_pokemon_names = [p['name'] for p in all_pokemon if search_letters in p['name']][
                                     offset:offset + limit]

            pokemon_details = []
            for name in filtered_pokemon_names:
                detail_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
                if detail_response.status_code == 200:
                    poke_data = detail_response.json()

                    # Fetch Pokemon species data for memo (description)
                    species_response = requests.get(poke_data['species']['url'])
                    species_data = species_response.json() if species_response.status_code == 200 else {}
                    description = next((entry['flavor_text'] for entry in species_data.get('flavor_text_entries', []) if
                                        entry['language']['name'] == 'en'), '')

                    # Extract special ability
                    special_ability = next(
                        (ability['ability']['name'] for ability in poke_data['abilities'] if ability['is_hidden']), '')

                    pokemon = {
                        'order': poke_data.get('order', 0),
                        'name': poke_data.get('name', ''),
                        'lvl': 1,  # Assuming default level 1
                        'xp': poke_data.get('base_experience', 0),
                        'number': poke_data.get('id', 0),
                        'type_1': poke_data['types'][0]['type']['name'] if poke_data['types'] else '',
                        'type_2': poke_data['types'][1]['type']['name'] if len(poke_data['types']) > 1 else '',
                        'special_capacity': special_ability,
                        'memo': description,
                        'atck': poke_data['stats'][1]['base_stat'] if len(poke_data['stats']) > 1 else 0,
                        'defs': poke_data['stats'][2]['base_stat'] if len(poke_data['stats']) > 2 else 0,
                        'atck_spe': poke_data['stats'][3]['base_stat'] if len(poke_data['stats']) > 3 else 0,
                        'defs_spe': poke_data['stats'][4]['base_stat'] if len(poke_data['stats']) > 4 else 0,
                        'speed': poke_data['stats'][5]['base_stat'] if len(poke_data['stats']) > 5 else 0,
                        'hp': poke_data['stats'][0]['base_stat'] if poke_data['stats'] else 0,
                        'team_id': 0,  # Assuming no team by default
                        'shiny': False,  # You might want to set this based on some condition
                        'image_url': poke_data['sprites']['front_default'],
                        'shiny_image_url': poke_data['sprites']['front_shiny']
                    }
                    pokemon_details.append(pokemon)

            return Response(pokemon_details)
    except requests.RequestException as e:
        # Proper logging of the exception
        return HttpResponseBadRequest({'message': 'Error in fetching data from PokeAPI'})
