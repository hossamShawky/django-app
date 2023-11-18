from django.db import models


class User(models.Model):
    name = models.CharField(max_length=15)

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=200)
 