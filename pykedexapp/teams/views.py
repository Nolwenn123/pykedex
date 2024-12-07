from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Team


# Request on sqlite database

@api_view(['GET'])
def get_all_teams(request):
    teams = Team.objects.all()
    return Response(teams.values())

@api_view(['GET'])
def get_team_by_user_id(request, user_id):
    teams = Team.objects.filter(user_id=user_id)
    return Response(teams.values())

@api_view(['POST'])
def post_team(request, user_id):
    team = Team.objects.create(
        name=request.data['name'],
        user_id=user_id,
    )
    return Response(team.values())

@api_view(['PUT'])
def put_team(request, id):
    team = Team.objects.get(id=id)
    team.name = request.data['name']
    team.save()
    return Response(team.values())

@api_view(['DELETE'])
def delete_team(request, id):
    team = Team.objects.get(id=id)
    team.delete()
    return Response(team.values())





