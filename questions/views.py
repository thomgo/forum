from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Topic

@login_required
def index(request):
    topics = Topic.objects.all()
    return render(request, "index.html", {"topics": topics})

@login_required
def user_questions(request):
    topics = Topic.objects.all()
    return render(request, "user_questions.html", {"topics": topics})
