from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponseServerError

import requests

def home(request):
  pokemon_list = []

  if 'search' in request.GET:
      search_term = request.GET['search'].lower()
      limit = request.GET['limit'].lower()
      offset = request.GET['offset'].lower()

      if limit == "" or offset == "":
          limit = "10"
          offset = "0"

      api_url_search_partial = f"http://localhost:8000/api/pokemons/pokeapi/get/some/" + search_term + "/" + limit + "/" + offset

      try:
          pokemon_req = requests.get(api_url_search_partial)
          pokemon_list = pokemon_req.json()
      except Exception as e:
          print(f"Error: {e}")
          return HttpResponseServerError("An error occurred while fetching Pokemon data.")

      context = {
          'pokemon_list': pokemon_list,
      }

      return render(request, 'home.html', context)

  return render(request, 'home.html')

def menu(request):
  template = loader.get_template('menu.html')
  return HttpResponse(template.render())

def signup(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username and password:
      api_url_register = "http://localhost:8000/api/users/auth/register/"

      try:
        response = requests.post(api_url_register, json={'username': username, 'password': password})

        if response.status_code == 201:
          # L'utilisateur a été créé avec succès
          return render(request, 'signin.html')
        else:
          # Affichez le message d'erreur de votre API
          error_message = response.json().get()
          return HttpResponseServerError(error_message. response.status_code)

      except Exception as e:
        print(f"Error: {e}")
        return HttpResponseServerError(e)

    else:
      return HttpResponseServerError("Missing username or password")
    
  return render(request, 'signup.html')

def signin(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username and password:
      api_url_login = "http://localhost:8000/api/users/auth/login/"
      try:
        response = requests.post(api_url_login, json={'username': username, 'password': password})
        if response.status_code == 200:
          # Connexion réussie
          return render(request, 'home.html')
        else:
          error_message = response.json().get('error', 'Invalid credentials')
          return HttpResponseServerError(f"{error_message} (status: {response.status_code})")

      except Exception as e:
        print(f"Error: {e}")
        return HttpResponseServerError(str(e))

    else:
      return HttpResponseServerError("Missing username or password")

  return render(request, 'signin.html')




def pokemon_view2(request):
  try:
    template = loader.get_template('pokemon_view2.html')

    if response.status_code == 200:
        # L'utilisateur a été créé avec succès
        return render(request, 'home.html')
    else:
        # Affichez le message d'erreur de votre API
        error_message = response.json().get()
        return HttpResponseServerError(error_message.response.status_code)

  except Exception as e:
    print(f"Error: {e}")
    return HttpResponseServerError(str(e))
  
  return render(request, 'signin.html')



def pokemon_view(request):
  template = loader.get_template('pokemon_view.html')
  return HttpResponse(template.render())

def team_view(request):
  pokemon_list = []
  team_list = []
  
  if 'user' in request.GET:
    user_id = request.GET['user'].lower()
    api_url_get_team = f"http://localhost:8000/api/teams/get/byuserid/" + user_id

    try:
      team_req = requests.get(api_url_get_team)
      team_list = team_req.json()
    except Exception as e:
      print(f"Error: {e}")
      return HttpResponseServerError("An error occurred while fetching Team data.")
    context = {
      'team_list': team_list,
    }
    return render(request, 'team_view.html', context)
  
  elif 'team' in request.GET and 'user' in request.GET:
    team_id = request.GET['team'].lower()
    api_url_get_team = f"http://localhost:8000/api/teams/get/byteamid/" + team_id
    api_url_get_team_pokemon = f"http://localhost:8000/api/pokemons/get/byteamid/" + team_id

    try:
      team_req = requests.get(api_url_get_team)
      team_list = team_req.json()
      pokemon_list_req = requests.get(api_url_get_team_pokemon)
      pokemon_list = pokemon_list_req.json()
    except Exception as e:
      print(f"Error: {e}")
      return HttpResponseServerError("An error occurred while fetching Team data.")
    context = {
      'user_id': request.GET['user'],
      'team_list': team_list,
      'pokemon_list': pokemon_list,
    }
    return render(request, 'team_view.html', context)
  return render(request, 'team_view.html')