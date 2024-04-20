from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include("account.urls"))
    # http://127.0.0.1:8000/api/v1/auth/signup
]

# telling django at which url and at which folder he need to find static data
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
