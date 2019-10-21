from django.db import models
from django import forms
from django.forms import ModelForm

from .models import Topic, Message

class TopicForm(ModelForm):
    """Form representing a topic entity for registration"""
    class Meta:
        model = Topic
        # we have only those fields since the other are not filled by the user
        fields = ['title', 'problem']

    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)
        # add class and translate labels for the different fields
        self.fields['title'].widget.attrs.update({'class': 'form-control',})
        self.fields['title'].label = "Votre question"
        self.fields['problem'].widget.attrs.update({'class': 'form-control',})
        self.fields['problem'].label = "Explication du problème"

class MessageForm(ModelForm):
    """Form representing a message entity for registration"""
    class Meta:
        model = Message
        # we have only those fields since the other are not filled by the user
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        # add class and translate labels for the different fields
        self.fields['content'].widget.attrs.update({'class': 'form-control',})
        self.fields['content'].label = "Votre message"
