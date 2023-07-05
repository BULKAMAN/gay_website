import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import CustomModel


class User(AbstractUser):
    id = models.UUIDField(verbose_name='Идентификатор пользователя', primary_key=True, default=uuid.uuid4, editable=False)


class Gym(CustomModel):
    name = models.CharField(verbose_name='Название gym\'a', editable=True, unique=True)
