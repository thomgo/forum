from django.db import models
from django.contrib.auth import get_user_model

class Topic(models.Model):
    """Class representing a Topic entity"""
    title = models.CharField(max_length=200)
    problem = models.TextField()
    # one to many relation, if and author is deleted all his topics are deleted by cascade
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    opening_date = models.DateTimeField(auto_now=True)
    is_solved = models.BooleanField(default=False)

class Message(models.Model):
    """Class representing a Message entity"""
    content = models.TextField()
    # one to many relation, if and author is deleted all his messages are deleted by cascade
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    publishing_date = models.DateTimeField(auto_now=True)
    # one to many relation, if a topic is deleted all the related messages are deleted by cascade
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
