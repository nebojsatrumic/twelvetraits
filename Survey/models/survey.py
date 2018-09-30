from libs.basemodel import BaseModel
from django.db import models

from django.core.validators import RegexValidator

only_alphabets_validator = RegexValidator(r'^[a-zA-Z_]+$', "Only alphabet characters allowed")


class Survey(BaseModel):
    name = models.CharField(max_length=100, validators=[only_alphabets_validator], default="")
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + " - " + self.name

    class Meta:
        verbose_name_plural = "Surveys"
