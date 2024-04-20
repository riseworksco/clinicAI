import logging

from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import Playlist, Song
from .serializers import PlaylistSerializer, SongSerializer


# Create your views here.
class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlaylistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]


def display_songs(request):
    items = Song.objects.all()
    context = {
        'items': items,
        'header': 'Multimedia Library'
    }
    logging.info(items)
    return render(request, "music/songs.html", context)


def index(request):
    return render(request, "music/index.html")


def recording_details(request):
    return render(request, "music/recordings-detail.html")
