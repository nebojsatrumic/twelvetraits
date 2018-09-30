from rest_framework import serializers

from Survey.models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        exclude = ('created_on', 'modified_on')
