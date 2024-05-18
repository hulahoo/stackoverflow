"""
Views

Types:
1. FBV(Function Based Views) -> views created by functions

URLs:
    1. http://localhost:8000/api/v1/auth/signup -> Resource url address that handles
    user signup logic
    2. http://localhost:8000/api/v1/auth/activation -> Resource url address that handles user activation

http://localhost:8000/api/v1/auth/signin -> URL address
http://localhost:8000/api/v1/auth/logout
http://localhost:8000/api/v1/auth/user/change

http://localhost:8000/api/v1/users/ - Get all users
http://localhost:8000/api/v1/users?filter[is_active]=True - Get all active users -> CustomUser.objects.filter(is_active=True) -> SELECT * FROM


"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from account.serializers import SignUpSerializer, ActivationSerializer


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


@api_view(['POST'])
def user_activation(request: Request):
    data = request.data
    serializer = ActivationSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(
            data={"message": f"Congrats! {request.data.get('email')} passed registration"},
            status=200
        )

