from django.db import models
from django import forms
from django.forms import ModelForm

from .models import Topic, Message

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'problem']

    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control',})
        self.fields['title'].label = "Votre question"
        self.fields['problem'].widget.attrs.update({'class': 'form-control',})
        self.fields['problem'].label = "Explication du problème"

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control',})
        self.fields['content'].label = "Votre message"

# class SearchForm(forms.Form):
#     search = forms.CharField(label='rechercher', max_length=100)
