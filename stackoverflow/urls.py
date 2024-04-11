from django.urls import path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
]

# telling django at which url and at which folder he need to find static data
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
