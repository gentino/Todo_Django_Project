from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description =models.TextField()
    done=models.BooleanField(default=False)
    created_at =models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)