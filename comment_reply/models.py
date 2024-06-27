from django.db import models


class CommentReply(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    reply = models.ForeignKey(
        "reply.Reply",
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        "account.CustomUser",
        on_delete=models.CASCADE,
        related_name="comments"
    )

    def __str__(self):
        return f"{self.id}:{self.message[:15]}"

    class Meta:
        db_table = "reply_comments"
        ordering = ["-created_at"]

