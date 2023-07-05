from django.contrib import admin

from tags_management.models import *


class TagAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'content',
        'creator',
        'create_date_time_stamp'
    ]
    search_fields = [
        'content'
    ]


class TagBinderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'tag',
        'bind_creator',
        'create_date_time_stamp',
        'tag_create_datetime_stamp'
    ]
    search_fields = [
        'tag'
    ]


admin.site.register(Tag, TagAdmin)
admin.site.register(TagBinder, TagBinderAdmin)
