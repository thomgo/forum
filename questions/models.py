from django.db import models
from django.contrib.auth import get_user_model

class Topic(models.Model):
    title = models.CharField(max_length=200)
    problem = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    opening_date = models.DateTimeField(auto_now=True)
    is_solved = models.BooleanField(default=False)

class Message(models.Model):
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    publishing_date = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
