from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('user/delete/<int:question_id>', views.delete_question, name='delete_question'),
    path('user', views.user_questions, name='user_questions'),
]
