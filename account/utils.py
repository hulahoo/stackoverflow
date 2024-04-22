import json

from django.core.mail import send_mail


def send_activation_code(email: str, activation_code: str) -> None:
    context = {
        "message": "Thank you for passing registration!",
        "email": email,
        "code": activation_code
    }
    send_mail(
        from_email="admin@gmail.com",
        subject="Signup verification",
        message=json.dumps(context),
        recipient_list=[email],
        fail_silently=False
    )
