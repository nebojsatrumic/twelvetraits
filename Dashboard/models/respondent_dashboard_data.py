from django.db import models

from libs.basemodel import BaseModel


class RespondentDashboardData(BaseModel):
    email = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=1000, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    openness = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    conscientiousness = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    extraversion = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    agreeableness = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    neuroticism = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Respondent Data"
