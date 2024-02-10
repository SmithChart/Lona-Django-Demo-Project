from django.db import models
from django.contrib.auth.models import User


class Demo(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.text}"
