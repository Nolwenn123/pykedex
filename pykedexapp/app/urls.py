from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
]
