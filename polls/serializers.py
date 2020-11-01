from django.contrib.auth.models import User	
from rest_framework import serializers
from polls.models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'author', 'status']


class ChoiceSerializer(serializers.ModelSerializer):

    question = serializers.SlugRelatedField(slug_field='question_text', read_only=True)

    class Meta:
        model = Choice
        fields = ['choice_text', 'question', 'votes']