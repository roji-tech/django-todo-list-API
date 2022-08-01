from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    # description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
