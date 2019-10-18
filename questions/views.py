from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import TopicForm, MessageForm

from .models import Topic

@login_required
def index(request):
    """Home view after login to display all unsolved and solved topics"""
    topics = Topic.objects.filter(is_solved=False)
    solved_topics = Topic.objects.filter(is_solved=True)
    return render(request, "index.html", {"topics": topics, "solved_topics": solved_topics})

@login_required
def single(request, topic_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = MessageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.topic = Topic.objects.get(id=topic_id)
            message.save()
    topic = Topic.objects.prefetch_related('message_set').get(id=topic_id)
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
    topics = Topic.objects.filter(author=request.user, is_solved=False)
    return render(request, "user_questions.html", {"topics": topics, 'form': form})

@login_required
def search(request):
    if request.method == 'POST':
        research = request.POST['search']
        topics = Topic.objects.filter(Q(title__icontains=research) | Q(problem__icontains=research))
    return render(request, "search.html", {'research': research, 'topics': topics})

@login_required
def archives(request):
    topics = Topic.objects.filter(author=request.user, is_solved=True)
    other_topics = Topic.objects.filter(is_solved=True).exclude(author=request.user)
    return render(request, "archives.html", {"topics": topics, 'other_topics': other_topics})

@login_required
def delete_question(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
        if request.user == topic.author:
            topic.delete()
    except Exception as e:
        pass
    return redirect('user_questions')

@login_required
def solve_question(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
        if request.user == topic.author:
            topic.is_solved = 1
            topic.save()
    except Exception as e:
        pass
    return redirect('user_questions')
