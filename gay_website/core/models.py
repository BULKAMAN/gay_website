import uuid

from django.db import models


class CustomModel(models.Model):
    id = models.UUIDField(verbose_name='Идентификатор пользователя', primary_key=True, default=uuid.uuid4, editable=False)
    objects = models.Manager()

    class Meta:
        abstract = True
