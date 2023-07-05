from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from gym.models import User, Gym


class GymAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name'
    ]
    search_fields = [
        'name'
    ]


admin.site.register(User, UserAdmin)
admin.site.register(Gym, GymAdmin)
