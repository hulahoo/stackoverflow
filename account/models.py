from django.db import models
from rest_framework import status
from django.utils.crypto import get_random_string
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        email: str | None,
        password: str | None,
        **extra_fields
    ):
        if not email:
            raise ValidationError(
                detail="Email not provided",
                code=status.HTTP_400_BAD_REQUEST
            )



class CustomUser(AbstractBaseUser):
    username = None

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=25, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f"{self.email}(ID={self.id})"

    def create_activation_code(self):
        code = get_random_string(
            length=25,
            allowed_chars="1234567890_+!@#$%^&*("
        )
        self.activation_code = code


# CustomUser.objects.filter(email="email") -> Queryset -> SQL Language(INSERT INTO customuser (...) VALUES (...))
# CustomUser.objects.first() -> Queryset -> SQL(SELECT * FROM ... WHERE email = "email")
# CustomUser.objects.get(email="email") -> Queryset
# CustomUser.objects.delete() -> Queryset
# CustomUser.objects.update_or_create() -> Queryset
