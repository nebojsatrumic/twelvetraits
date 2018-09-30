from rest_framework import serializers

from Survey.models import Respondent


class RespondentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Respondent
        exclude = ('created_on', 'modified_on')
