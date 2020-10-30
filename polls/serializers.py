from django.contrib.auth.models import User	
from rest_framework import serializers
from polls.models import Question


class QuestionSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'author', 'status']