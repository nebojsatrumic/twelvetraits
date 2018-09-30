from rest_framework import serializers

from Dashboard.models.respondent_dashboard_data import RespondentDashboardData


class RespondentDashboardDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespondentDashboardData
        exclude = ('created_on', 'modified_on')
