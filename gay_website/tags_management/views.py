from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from tags_management.models import Tag
from tags_management.serializers import TagFullSerializer


class TagCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        serializer = TagFullSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            content = serializer.validated_data['content']
            creator = request.user
            tag = Tag.objects.filter(content=content).first()
            if not tag:
                tag = Tag(content=content, creator=creator)
                tag.save()
                response = model_to_dict(tag)
                response['creator'] = tag.creator.username
                return Response(data=response, status=201)
            else:
                return Response(data={'Error': 'Tag with such content is already exist'}, status=400)
