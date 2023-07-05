from django.urls import path

from tags_management.views import TagCreate

urlpatterns = [
    path('tag/create', TagCreate.as_view()),
]
