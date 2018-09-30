from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from Survey.models import Answer
from Survey.serializers import RespondentAnswerSerializer


class RespondentAnswerViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = Answer.objects.all()
    serializer_class = RespondentAnswerSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = Answer.objects.filter(respondent=kwargs['parent_lookup_respondent']).all()
        return super().list(request, *args, **kwargs)