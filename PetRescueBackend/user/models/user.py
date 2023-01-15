import uuid
from django.db import models

from PetRescueBackend.core.models import BaseModel


class User(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=64
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=64
    )

    password = models.CharField(
        blank=False,
        null=False,
        max_length=17
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} (User)'
