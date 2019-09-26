from django.conf.urls import url

from . import views

urlpatterns = [
    url("index", views.index, name='index'),
    url("user", views.user_questions, name='user_questions'),
]
