from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    published_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="post", default="post/1.png")
    tags = models.ManyToManyField(to=Tag)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    published_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id)
