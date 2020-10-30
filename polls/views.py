
from django.http import HttpResponse
from django.http import Http404
from polls.models import Question, Choice

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView

from polls.serializers import QuestionSerializer, ChoiceSerializer
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = QuestionSerializer

    def get_object(self):
        return get_object_or_404(Question, pk=self.kwargs.get('question_id'))


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all().order_by('-votes')
    serializer_class = ChoiceSerializer


class ChoiceDetail(APIView):
    
    serializer_class = ChoiceSerializer

    def get_object(self):
        return get_object_or_404(Choice, pk=self.kwargs.get('choice_id'))