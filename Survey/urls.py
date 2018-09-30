from django.conf.urls import url, include
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_swagger.views import get_swagger_view
from Survey import views

router = ExtendedSimpleRouter()

# router.register(r'respondent', views.RespondentViewSet)
router.register(r'respondent', views.RespondentViewSet).register(r'answers',
                                                                 views.RespondentAnswerViewSet,
                                                                 base_name='respondent-answers',
                                                                 parents_query_lookups=['respondent'])
router.register(r'answer', views.AnswerViewSet)

schema_view = get_swagger_view(title='Survey API')

urlpatterns = [
    # url(r'^test/', TestView.as_view()),
    url(r'^', include(router.urls)),
]
