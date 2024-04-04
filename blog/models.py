from django.db import models
from account.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    img = models.ImageField(upload_to='blog/')
    c_date = models.DateTimeField(auto_now_add=True)
    u_date = models.DateTimeField(auto_now=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

