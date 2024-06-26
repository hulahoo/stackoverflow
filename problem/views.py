"""
CRUD Actions:
1. Create Problem/Reply/ReplyComment
2. Read Problem/Reply/ReplyComment
3. Update Problem/Reply/ReplyComment
4. Delete Problem/Reply/ReplyComment

Views

Types:
1. FBV(Function Based Views) -> views created using functions
2. CBV(Class Based Views) -> views created using OOP(classes)
    a. APIView: rest_framework.views.APIView -> the incoming request is dispatched to an appropriate handler method such as .get() or .post().
    b. Generics: rest_framework.generics -> The generic views provided by REST framework allow you to quickly build API views that map closely to your database models.


URLs:
    1. POST 127.0.0.1:8000/api/v1/problems/ - create problem
    2. GET 127.0.0.1:8000/api/v1/problems/ - list all problems
    3. GET 127.0.0.1:8000/api/v1/problems/{:problem_id}/ - get problem details by its id

Authentification
Request to create problem -> request.data, request.user check if user is_active=True and user exists in database
Request: data, user

If user authenticated -> request.user = CustomUser
"""
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from .models import Problem
from .serializers import (
    ProblemSerializer,
    ListProblemSerializer,
    DetailProblemSerializer,
    UpdateProblemSerializer
)
from permissions.problem import IsAuthorPermission

# Creating Problem
class CreateProblemView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        data = request.data
        pictures = request.FILES
        problem_serializer = ProblemSerializer(
            data=data,
            context={
                "pictures": pictures,
                "user": request.user
            }
        )
        if problem_serializer.is_valid(raise_exception=True):
            problem_serializer.save()
            return Response(
                data={"data": problem_serializer.data},
                status=201
            )

# Reading all problems
class ListProblemView(ListAPIView):
    queryset = Problem.objects.all()
    serializer_class = ListProblemSerializer
    permission_classes = [IsAuthenticated]

    # def get_serializer_context(self): # to pass extra context to serializer
        # return super().get_serializer_context()

# Reading single problem instance
class DetailProblemView(RetrieveAPIView):
    lookup_field = "pk"
    permission_classes = [IsAuthenticated]
    queryset = Problem.objects.all()
    serializer_class = DetailProblemSerializer

# Destroy(Delete) single problem instance
# Permission: Only author of a problem can delete problem => if request.user == problem.author: True else False
class DestroyProblemView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAuthorPermission]
    queryset = Problem.objects.all()


class UpdateProblemView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAuthorPermission]
    queryset = Problem.objects.all()
    serializer_class = UpdateProblemSerializer

