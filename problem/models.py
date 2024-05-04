from django.db import models


class Problem(models.Model):
    title = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    author = models.ForeignKey(
        'account.CustomUser',
        on_delete=models.CASCADE,
        related_name="problems"
    )

    def __str__(self) -> str:
        return f"{self.id}:{self.title}"
    
    class Meta:
        db_table = "problems"
        ordering = ["-created_at"]
        # ordering = ["-created_at"] -> DESCENDING
        # ordering = ["created_at"] -> ASCENDING

# user = CustomUser.objects.filter(id=1)
# user.problems.all() -> return all user created problems

class Picture(models.Model):
    image = models.ImageField(upload_to="problemPictures")

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name="pictures"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Picture.{self.id}:{self.problem}"

    class Meta:
        db_table = "problem_pictures"
        ordering = ["-created_at"]


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


class CommentReply(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    reply = models.ForeignKey(
        Reply,
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
