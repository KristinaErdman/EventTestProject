from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from events.urls import events_router
from users.urls import users_router

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('users/', include(users_router.urls)),
                  path('events/', include(events_router.urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
