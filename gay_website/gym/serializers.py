from rest_framework import serializers

from gym.models import Gym


class GymFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ['id', 'name']
