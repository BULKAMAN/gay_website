from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from gym.models import Gym
from gym.serializers import GymFullSerializer


class GymCreate(generics.CreateAPIView):
    serializer_class = GymFullSerializer
    permission_classes = [IsAuthenticated]
    queryset = Gym.objects.all()
