from django.db import models

from Survey.models.question import Question
from Survey.models.respondent import Respondent
from .basemodel import BaseModel


class Answer(BaseModel):
    answer_text = models.CharField(max_length=100, default="")
    question = models.ForeignKey(Question, related_name='question_answers', on_delete=models.CASCADE)
    respondent = models.ForeignKey(Respondent, related_name='user_answers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('respondent', 'question',)
        verbose_name_plural = "Answers"


    def __str__(self):
        return str(self.id) + " - " + self.answer_text

