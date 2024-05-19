from django.urls import path

from .views import (
    ListProblemView,
    CreateProblemView,
    DetailProblemView,
    DestroyProblemView,
    UpdateProblemView
)

urlpatterns = [
    path("", CreateProblemView.as_view()),
    path("list/", ListProblemView.as_view()),
    path("<pk>/", DetailProblemView.as_view()),
    path("<pk>/delete/", DestroyProblemView.as_view()),
    path("<pk>/update/", UpdateProblemView.as_view())
]

# <pk> -> 127.0.0.1:8000/api/v1/problems/1/
# <pk> -> 127.0.0.1:8000/api/v1/problems/2/
# <pk> -> 127.0.0.1:8000/api/v1/problems/3/