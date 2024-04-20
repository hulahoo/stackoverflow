"""
Views

Types:
1. FBV(Function Based Views) -> views created by functions

http://localhost:8000/api/v1/auth/signup -> Resource url address that handles user signup logic
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


@api_view()
def signup(request: Request):
    print(dir(request))
    # dir(object) - returns all methods and attributes from object
    return Response(
        data={"message": "Success"},
        status=200
    )
