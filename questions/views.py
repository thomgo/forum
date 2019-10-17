from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import TopicForm, MessageForm

from .models import Topic

@login_required
def index(request):
    topics = Topic.objects.filter(is_solved=False)
    return render(request, "index.html", {"topics": topics})

@login_required
def single(request, question_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = MessageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.topic = Topic.objects.get(id=question_id)
            message.save()
    topic = Topic.objects.prefetch_related('message_set').get(id=question_id)
    form = MessageForm()
    return render(request, "single.html", {"topic": topic, 'form': form})

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
    topics = Topic.objects.filter(author=request.user)
    return render(request, "user_questions.html", {"topics": topics, 'form': form})

@login_required
def delete_question(request, question_id):
    try:
        topic = Topic.objects.get(id=question_id)
        if request.user == topic.author:
            topic.delete()
    except Exception as e:
        pass
    return redirect('user_questions')

@login_required
def solve_question(request, question_id):
    try:
        topic = Topic.objects.get(id=question_id)
        if request.user == topic.author:
            topic.is_solved = 1
            topic.save()
    except Exception as e:
        pass
    return redirect('user_questions')
