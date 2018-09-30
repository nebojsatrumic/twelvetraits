from rest_framework import serializers

from Survey.models import Answer
from Survey.serializers import RespondentSerializer


class RespondentAnswerSerializer(serializers.ModelSerializer):
    respondent = RespondentSerializer(required=False)

    class Meta:
        model = Answer
        fields = '__all__'
