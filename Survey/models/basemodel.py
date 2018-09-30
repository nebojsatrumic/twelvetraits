from django.db import models


class BaseModel(models.Model):
    """Base model inherited by all other models"""

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True, auto_created=True)

    class Meta:
        abstract = True
