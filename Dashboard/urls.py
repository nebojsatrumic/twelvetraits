from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from Dashboard.views import DashboardlView

urlpatterns = [
    url(r'^dashboard/', DashboardlView.as_view()),
]
