from rest_framework import serializers

from reply.models import Reply


class ReplySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.email")

    class Meta:
        model = Reply
        fields = "__all__"

    def create(self, validated_data: dict) -> Reply:
        request = self.context.get("request")

        reply = Reply.objects.create(
            author=request.user,
            **validated_data
        )

        return reply
