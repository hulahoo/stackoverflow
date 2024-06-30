"""
Django Rest Framework serializers type:

1. Serializer
2. ModelSerializer
"""
from datetime import datetime

from rest_framework import serializers

from .models import Problem, Picture
from reply.serializers import ReplySerializer


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ("id", "image", "problem")
        read_only_fields = ("id", )


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ["title", "description", "author", "id"]
        read_only_fields = ["id", "author"]

    def create_pictures(self, pictures: list, problem: Problem):
        for picture in pictures.getlist("picture"):
            serializer = PictureSerializer(
                data={
                    "image": picture,
                    "problem": problem.id
                }
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    def create(self, validated_data: dict) -> Problem:
        validated_data["author"] = self.context["user"]

        problem = Problem.objects.create(**validated_data)
        pictures = self.context.get("pictures", [])

        if pictures:
            self.create_pictures(pictures, problem)

        return problem


class ListProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ("id", "title", "description", "author", "created_at")


class DetailProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = "__all__"

    def to_representation(self, instance: Problem):
        representation = super().to_representation(instance)
        pictures = PictureSerializer(
            instance.pictures.all(),
            many=True
        )
        replies = ReplySerializer(
            instance.replies.all(),
            many=True
        )
        representation["replies"] = replies.data
        representation["pictures"] = pictures.data
        return representation


class UpdateProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ("title", "description", "id", "author", "modified_at")
        read_only_fields = ("id", "author", "modified_at")

    def update(self, instance: Problem, validated_data: dict):
        instance = super().update(instance, validated_data)
        instance.modified_at = datetime.now()
        instance.save()
        return instance
