from django.urls import path

from account.views import signup


urlpatterns = [
    path("signup/", signup)
]
