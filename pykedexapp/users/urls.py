from django.urls import path
from . import views

urlpatterns = [
    path('auth/register/', views.register, name='users_register'),
    path('auth/login/', views.login, name='users_login'),
    path('auth/logout/', views.logout, name='users_logout'),
    path('update/<int:id>', views.update, name='users_update'),
    path('get/all/', views.get_all, name='users_get_all'),
    path('get/one/<int:id>', views.get_one, name='users_get_one'),
]
