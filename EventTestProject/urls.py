from django.contrib import admin
from django.urls import path, include

from events.urls import events_router
from users.urls import users_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(users_router.urls)),
    path('events/', include(events_router.urls)),
]
