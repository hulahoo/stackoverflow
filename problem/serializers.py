"""
Django Rest Framework serializers type:

1. Serializer
2. ModelSerializer
"""

from rest_framework import serializers

from .models import Problem, Picture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ("id", "image", "problem")
        read_only_fields = ("id", )


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ["title", "description", "author"]

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
        representation["pictures"] = pictures.data
        return representation
