from django.db import models


class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __repr__(self):
        return f'{self.__class__.__name__}'

    def __str__(self):
        return f'{self.__class__.__name__}'