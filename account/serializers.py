from rest_framework import serializers

from account.models import CustomUser
from account.utils import send_activation_code


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
        user: CustomUser = CustomUser.objects.create_user(**validated_data)
        # send mail
        send_activation_code(
            email=user.email,
            activation_code=user.activation_code
        )
        return user


class ActivationSerializer(serializers.Serializer):
    """
    Serializer for validatin activation request
    """
    email = serializers.EmailField(required=True)
    code = serializers.CharField(min_length=25, required=True)

    def validate(self, attrs: dict[str, str]):
        user = CustomUser.objects.filter(
            email=attrs.get("email"), activation_code=attrs.get("code")
        ).first()

        if not user:
            raise serializers.ValidationError(
                detail="Provided information is invalid",
                code=400
            )
        attrs["user"] = user
        return attrs

    def create(self, validated_data: dict[str, str]):
        user: CustomUser = validated_data.pop("user")
        user.is_active = True
        user.activation_code = ''
        user.save()
        return user

# serializer = SignUpSerializer(email="tof@gmail.com", password="1234", password_confirmation="12345")

# serializer.is_valid() # calls serializer.validate() ... calls validation on each field

# serializer.save()
