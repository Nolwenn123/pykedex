from django.urls import path

from . import views

urlpatterns = [
    # [GET] API
    # The following are the endpoints for the API (teams saved in the database)
    path('get/all', views.get_all_teams),
    path('get/byuserid/<int:user_id>/', views.get_team_by_user_id),

    # [POST] API
    # Teams are saved because they are created
    path('post/for_this_user/<int:user_id>', views.post_team),

    # [PUT] API
    # Teams are updated because they are edited
    path('put/<int:id>', views.put_team),

    # [DELETE] API
    # Teams are deleted because they are removed
    # But it needs to delete the pokemons in the team first
    path('delete/with_pokemons/<int:id>', views.delete_team),
]
