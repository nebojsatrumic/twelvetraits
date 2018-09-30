from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from Survey.models import Answer
from Survey.serializers import AnswerSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
