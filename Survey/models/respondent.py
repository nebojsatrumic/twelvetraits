from django.core.validators import EmailValidator
from django.db import models

from .basemodel import BaseModel


class Respondent(BaseModel):
    ip_address = models.CharField(max_length=50)
    session_id = models.CharField(max_length=100)
    email = models.CharField(max_length=100, validators=[EmailValidator(message="Enter a valid email address")])
    location = models.CharField(max_length=1000, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Respondent Data"
