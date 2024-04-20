"""
Views

Types:
1. FBV(Function Based Views) -> views created by functions

http://localhost:8000/api/v1/auth/signup -> Resource url address that handles
user signup logic
http://localhost:8000/api/v1/auth/signin
http://localhost:8000/api/v1/auth/logout
http://localhost:8000/api/v1/auth/user/change

"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from account.serializers import SignUpSerializer


@api_view(['POST'])
def signup(request: Request):
    data = request.data
    serializer = SignUpSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(
            data={"message": "Successfully registered"},
            status=201
        )
