from rest_framework import serializers

from account.models import CustomUser


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        min_length=4, required=True
    )
    password_confirmation = serializers.CharField(
        min_length=4, required=True
    )

    def validate(self, attrs: dict[str, str]):
        """
            data: {"email": ..., "password": ..., "password_confirmation": ...}
        """
        password = attrs.get("password")
        password_confirmation = attrs.pop("password_confirmation")

        if password != password_confirmation:
            raise serializers.ValidationError(
                detail="Passwords didn't match",
                code=400
            )
        return attrs

    def create(self, validated_data: dict[str, str]) -> CustomUser:
        """
        validated_data is a data that returned from self.validate() function
        """
        print(validated_data)
        user = CustomUser.objects.create_user(**validated_data)
        return user



# serializer = SignUpSerializer(email="tof@gmail.com", password="1234", password_confirmation="12345")

# serializer.is_valid() # calls serializer.validate() ... calls validation on each field

# serializer.save()

