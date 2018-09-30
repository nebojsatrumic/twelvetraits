from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Dashboard.models.respondent_dashboard_data import RespondentDashboardData
from Dashboard.serializers.respondet_dashboard_data_serializer import RespondentDashboardDataSerializer
from ..services.external_services import ExternalService, GoogleSurveyService, FacebookSurveyService

EXTERNAL_SERVICES = [ExternalService,
                     GoogleSurveyService,
                     FacebookSurveyService, ]
DEFAULT_LIMIT = 100


class DashboardlView(APIView):
    """Dashboard interactions"""
    permission_classes = (AllowAny,)

    def get(self, request):
        """
        API endpoint to display the aggregated information

        :param query_params: ?limit=10&email=test@test.com
        :return: json response
        """
        limit = int(request.query_params.get('limit', DEFAULT_LIMIT))
        filter = self.request.query_params
        # Very bad way to do this but it will do just for now
        filter_params = {}
        for key in filter:
            if key != 'limit':
                filter_params.update({key: filter[key]})
        queryset = RespondentDashboardData.objects.filter(**filter_params).all().order_by('-email')[:limit]
        serializer = RespondentDashboardDataSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        API endpoint to export data from different survey services and persist it

        :param request: {"email": "neko@nesto.com"}
        :return: 200 OK
        """

        for service in EXTERNAL_SERVICES:
            respondent_dashboard_data = service.retrieve_respondat_survey_data(request.data['email'])

            for data in respondent_dashboard_data:
                new_resp_data = RespondentDashboardData(email=data['email'],
                                                        location=data['location'],
                                                        phone_number=data['phone_number'])
                new_resp_data.save()

        return Response()
