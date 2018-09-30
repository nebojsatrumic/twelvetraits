from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from Survey.models import Respondent
from Survey.serializers import RespondentSerializer


class RespondentViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer
