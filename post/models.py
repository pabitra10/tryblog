from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField(max_length=100)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:20] + "..."