from rest_framework import serializers

from comment_reply.models import CommentReply


class CommentReplySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.email")

    class Meta:
        model = CommentReply
        fields = "__all__"

    def create(self, validated_data: dict):
        request = self.context.get("request")
        comment = CommentReply.objects.create(
            author=request.user,
            **validated_data
        )
        return comment
