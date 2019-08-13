from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    body = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
