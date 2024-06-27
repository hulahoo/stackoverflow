"""
Types:
1. FBV(Function Based Views) -> views created using functions
2. CBV(Class Based Views) -> views created using OOP(classes)
    a. APIView: rest_framework.views.APIView -> the incoming request is dispatched to an appropriate handler method such as .get() or .post().

    b. Generics: rest_framework.generics -> The generic views provided by REST framework allow you to quickly build API views that map closely to your database models.

    c. ModelViewSets: rest_framework.viewsets -> Allow us to combine the logic for a set of related views into a single class. Viewsets doesnt provide any method handlers such as .get(), .post(), .delete(), instead it provides `actions`: .list(), .create(), .destroy(), .partial_update(), .patch()
    Typically, rather than explicitly registering the views in a viewset in the urlconf(urls.py), we will register the viewset with a `router class`, that automatically determines the urlconf for us
"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from reply.models import Reply
from reply.serializers import ReplySerializer


class ReplyViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [IsAuthenticated]
