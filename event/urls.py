
from django.contrib import admin

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from cor_events import urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('events/', include('cor_events.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)