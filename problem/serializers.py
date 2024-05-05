"""
Django Rest Framework serializers type:

1. Serializer
2. ModelSerializer
"""

from rest_framework import serializers

from .models import Problem, Picture


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ["title", "description", "author"]

    def create(self, validated_data: dict) -> Problem:
        problem = Problem.objects.create(**validated_data)
        pictures = self.context.get("pictures", [])

        if pictures:
            for picture in pictures.getlist("picture"):
                Picture.objects.create(
                    image=picture,
                    problem=problem
                )
        return problem
