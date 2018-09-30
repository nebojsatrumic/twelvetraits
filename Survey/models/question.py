from Survey.models.survey import Survey
from libs.basemodel import BaseModel
from django.db import models


class Question(BaseModel):
    question_text = models.CharField(max_length=100, default="")
    survey = models.ForeignKey(Survey, related_name='survey_questions', on_delete=models.CASCADE)
    ordinal_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id) + " - " + self.question_text

    class Meta:
        verbose_name_plural = "Questions"
