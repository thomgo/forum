from django.db import models
from django.forms import ModelForm

from .models import Topic

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'problem']
