from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import TopicForm

from .models import Topic

@login_required
def index(request):
    topics = Topic.objects.all()
    return render(request, "index.html", {"topics": topics})

@login_required
def user_questions(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = TopicForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
    form = TopicForm()
    topics = Topic.objects.all()
    return render(request, "user_questions.html", {"topics": topics, 'form': form})

@login_required
def delete_question(request, question_id):
    return HttpResponse("Coucou")
