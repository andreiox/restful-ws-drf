from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView, Response
from rest_framework.pagination import PageNumberPagination
from .models import Song
from .serializers import SongSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Song.objects.all().order_by('id')

        name = self.request.query_params.get('name', None)
        album = self.request.query_params.get('album', None)
        artist = self.request.query_params.get('artist', None)

        if name is not None:
            queryset = queryset.filter(name=name)
        if album is not None:
            queryset = queryset.filter(album=album)
        if artist is not None:
            queryset = queryset.filter(artist=artist)

        return queryset


class CustomView(APIView):
    def get(self, request, format=None):
        return Response("Some Get Response")

    def post(self, request, format=None):
        return Response("Some Post Response")
