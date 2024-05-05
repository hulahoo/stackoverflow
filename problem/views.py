"""
CRUD:
1. Create Problem/Reply/ReplyComment
2. Read Problem/Reply/ReplyComment
3. Update Problem/Reply/ReplyComment
4. Delete Problem/Reply/ReplyComment

Views

Types:
1. FBV(Function Based Views) -> views created using functions
2. CBV(Class Based Views) -> views created using OOP(classes)
    a. rest_framework.views.APIView -> the incoming request is dispatched to an appropriate handler method such as .get() or .post().

URLs:
    1. POST 127.0.0.1:8000/api/v1/problems/ - create problem
    2. GET 127.0.0.1:8000/api/v1/problems/ - list all problems
    3. GET 127.0.0.1:8000/api/v1/problems/{:problem_id}/ - get problem details by its id
"""

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import ProblemSerializer


class CreateProblemView(APIView):

    def post(self, request: Request):
        data = request.data
        pictures = request.FILES
        print(pictures)
        problem_serializer = ProblemSerializer(
            data=data,
            context={"pictures": pictures}
        )
        if problem_serializer.is_valid(raise_exception=True):
            problem_serializer.save()
            return Response(
                data={"data": problem_serializer.data},
                status=201
            )
