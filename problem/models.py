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
