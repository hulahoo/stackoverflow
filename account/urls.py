from django.urls import path

from account.views import signup, user_activation


urlpatterns = [
    path("signup/", signup),
    path("activation/", user_activation)
]
