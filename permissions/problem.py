from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from problem.models import Problem

class IsAuthorPermission(BasePermission):
    def has_object_permission(
        self,
        request: Request,
        view: APIView,
        obj: Problem
    ):
        return request.user == obj.author