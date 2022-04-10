from rest_framework import routers

from .views import ManagerViewSet

users_router = routers.SimpleRouter()

users_router.register(r'managers', ManagerViewSet, basename='managers')
