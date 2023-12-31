# Generated by Django 4.2.2 on 2023-06-13 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Идентификатор пользователя')),
                ('content', models.CharField(max_length=1000, unique=True, verbose_name='Контент')),
                ('create_date_time_stamp', models.DateTimeField(auto_now_add=True, verbose_name='Создан (дата)')),
                ('publication_start_date_time_stamp', models.DateTimeField(verbose_name='Начало публикации (дата)')),
                ('publication_stop_date_time_stamp', models.DateTimeField(verbose_name='Конец публикации (дата)')),
                ('block_date_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='Время блокировки')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'db_table': 'table_01_tag',
            },
        ),
        migrations.CreateModel(
            name='TagBinder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Идентификатор пользователя')),
                ('create_date_time_stamp', models.DateTimeField(auto_now_add=True)),
                ('bind_creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags_management.tag')),
            ],
            options={
                'verbose_name': 'Связка тега',
                'verbose_name_plural': 'Связки тегов',
                'db_table': 'table_01_tag_binders',
            },
        ),
    ]
