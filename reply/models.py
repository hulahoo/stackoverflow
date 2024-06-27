from django.db import models

from problem.models import Problem


class Reply(models.Model):
    message = models.TextField()
    image = models.ImageField(upload_to="replyImages")

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name="replies"
    )
    author = models.ForeignKey(
        "account.CustomUser",
        on_delete=models.CASCADE,
        related_name="replies"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.id}:{self.message[:15]}"
    
    class Meta:
        db_table = "replies"
        ordering = ["-created_at"]
