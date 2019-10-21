from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.decorators.http import require_http_methods

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
    """View to display single topic information with messages, and allow users to answer"""
    # if this is a POST request we need to process the form data to register the message
    if request.method == 'POST':
        # hydrate a form object with data from the request
        form = MessageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # get the message object from the form, add some info and save it in DB
            message = form.save(commit=False)
            message.author = request.user
            message.topic = Topic.objects.get(id=topic_id)
            message.save()
    # Once the form is treated, we select the topic with all the related messages
    topic = Topic.objects.prefetch_related('message_set').get(id=topic_id)
    form = MessageForm()
    return render(request, "single.html", {"topic": topic, 'form': form})

@login_required
def user_questions(request):
    """View to diplay topics created by the logged user and allow topics creation"""
    # if this is a POST request we need to process the form data to register the topic
    if request.method == 'POST':
        # hydrate a form object with data from the request
        form = TopicForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # get the topic object from the form and persist it to DB
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
    # Create the form to be displayed in template and select the topics from the logged user
    form = TopicForm()
    topics = Topic.objects.filter(author=request.user, is_solved=False)
    return render(request, "user_questions.html", {"topics": topics, 'form': form})


@require_http_methods(["POST"])
@login_required
def search(request):
    """View only accessible by post to search for a topic based on a string input"""
    # get back the data from the search form
    research = request.POST['search']
    # search for topics
    topics = Topic.objects.filter(Q(title__icontains=research) | Q(problem__icontains=research))
    return render(request, "search.html", {'research': research, 'topics': topics})

@login_required
def archives(request):
    """View to display all solved topics"""
    # get the topics from the logged user
    topics = Topic.objects.filter(author=request.user, is_solved=True)
    # get all the topics not from the logged user
    other_topics = Topic.objects.filter(is_solved=True).exclude(author=request.user)
    return render(request, "archives.html", {"topics": topics, 'other_topics': other_topics})

@require_http_methods(["GET"])
@login_required
def delete_topic(request, topic_id):
    """View to delete a topic from DB"""
    try:
        # make sur the id match a topic and the author is the user
        topic = Topic.objects.get(id=topic_id)
        if request.user == topic.author:
            topic.delete()
    except Exception as e:
        pass
    return redirect('user_questions')

@require_http_methods(["GET"])
@login_required
def solve_topic(request, topic_id):
    """View to update a question as solved in DB"""
    try:
        # make sur the id match a topic and the author is the user
        topic = Topic.objects.get(id=topic_id)
        if request.user == topic.author:
            # mark the topic as solved
            topic.is_solved = 1
            topic.save()
    except Exception as e:
        pass
    return redirect('user_questions')
