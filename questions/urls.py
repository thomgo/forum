from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('single/<int:topic_id>', views.single, name='single'),
    path('user', views.user_questions, name='user_questions'),
    path('search', views.search, name='search'),
    path('archives', views.archives, name='archives'),
    path('user/delete/<int:topic_id>', views.delete_question, name='delete_question'),
    path('user/solve/<int:topic_id>', views.solve_question, name='solve_question'),
]
