from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('question/', views.QuestionList.as_view(), name='question_list'),
    path('question/<int:question_id>/', views.QuestionDetail.as_view(), name='question_details'),
]
