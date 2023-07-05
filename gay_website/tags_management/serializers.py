from rest_framework import serializers

from tags_management.models import Tag


class TagFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'content']
