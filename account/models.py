from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    username = None

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=25, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

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
