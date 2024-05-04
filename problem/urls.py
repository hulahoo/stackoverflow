from django.urls import path

from .views import CreateProblemView

urlpatterns = [
    path("", CreateProblemView.as_view())
]