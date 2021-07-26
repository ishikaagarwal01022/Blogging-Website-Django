# from home.models import Blogs
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Blogs(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    subtitle = models.TextField()
    slug = models.TextField()
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.sno) + self.title


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:10] + "... by " + self.user.username