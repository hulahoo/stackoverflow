"""
Models
"""

from django.db import models
from rest_framework import status
from django.utils.crypto import get_random_string
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):

    def _perform_create(
        self,
        email: str | None,
        password: str | None,
        **extra_fields
    ) -> "CustomUser":
        if not email or password:
            raise ValidationError(
                detail="Authorization data invalid",
                code=status.HTTP_400_BAD_REQUEST
            )
        email = self.normalize_email(email)
        user: "CustomUser" = self.model(email=email, **extra_fields)
        # {"email": "tof@gmail.com", "is_active": False, "activation_code": ""}
        user.set_password(password)
        return user

    def create_user(
        self,
        email: str | None,
        password: str | None,
        **extra_fields
    ) -> "CustomUser":
        user = self._perform_create(email, password, **extra_fields)
        # {"email": "tof@gmail.com", "is_active": False, "activation_code": "", "password": "2fasdfdi9sfhs"}
        user.create_activation_code()
        # {"email": "tof@gmail.com", "is_active": False, "activation_code": "fadslkfnlksdf091", "password": "2fasdfdi9sfhs"}
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email: str | None,
        password: str | None,
        **extra_fields
    ) -> "CustomUser":
        user = self._perform_create(email, password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


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

    class Meta:
        db_table = "customuser"

# CustomUser.objects.create_user(email, password)
# CustomUser.objects.filter(email="email") -> Queryset -> SQL Language(INSERT INTO customuser (...) VALUES (...))
# CustomUser.objects.first() -> Queryset -> SQL(SELECT * FROM ... WHERE email = "email")
# CustomUser.objects.get(email="email") -> Queryset
# CustomUser.objects.delete() -> Queryset
# CustomUser.objects.update_or_create() -> Queryset
