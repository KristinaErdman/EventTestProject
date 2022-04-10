from rest_framework import routers

from .views import FirstTypeEventViewSet, SecondTypeEventViewSet, ApplicationViewSet, FeedbackViewSet

events_router = routers.SimpleRouter()

events_router.register(r'first_type_events', FirstTypeEventViewSet, basename='first_type_events')
events_router.register(r'applications', ApplicationViewSet, basename='application')
events_router.register(r'second_type_events', SecondTypeEventViewSet, basename='second_type_events')
events_router.register(r'feedbacks', FeedbackViewSet, basename='feedbacks')
