from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from comment_reply.models import CommentReply
from comment_reply.serializers import CommentReplySerializer


class CommentReplyViewSet(ModelViewSet):
    queryset = CommentReply.objects.all()
    serializer_class = CommentReplySerializer
    permission_classes = [IsAuthenticated]
