from django.urls import path

from gym.views import *

urlpatterns = [
    path('gym/create', GymCreate.as_view()),
]
