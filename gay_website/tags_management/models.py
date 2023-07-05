from django.db import models

from core.models import CustomModel
from gym.models import User

from django.contrib import admin


class Tag(CustomModel):
    content = models.CharField(max_length=1000, unique=True, verbose_name='Контент')
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Создатель'
    )
    create_date_time_stamp = models.DateTimeField(
        verbose_name='Создан (дата)',
        auto_now_add=True
    )
    publication_start_date_time_stamp = models.DateTimeField(
        verbose_name='Начало публикации (дата)',
        null=True,
        blank=True
    )
    publication_stop_date_time_stamp = models.DateTimeField(
        verbose_name='Конец публикации (дата)',
        null=True,
        blank=True
    )
    block_date_time_stamp = models.DateTimeField(
        verbose_name='Время блокировки',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'table_01_tag'
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


#############################################################
# Tag Binder area
class TagBinder(CustomModel):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Тег')
    bind_creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Создатель')
    create_date_time_stamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата привязки')

    @admin.display(description="Время создания тега")
    def tag_create_datetime_stamp(self):
        return str(self.tag.create_date_time_stamp)

    class Meta:
        db_table = 'table_01_tag_binders'
        verbose_name = 'Связка тега'
        verbose_name_plural = 'Связки тегов'
