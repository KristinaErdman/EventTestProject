from rest_framework import routers

from .views import ManagerViewSet, GuestViewSet

users_router = routers.SimpleRouter()

users_router.register(r'managers', ManagerViewSet, basename='managers')
users_router.register(r'guests', GuestViewSet, basename='guests')
