from rest_framework import serializers

from .models import Playlist, Song


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title", "youtube_link", "music_link"]


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields = ["id", "name", "songs"]


# music_management/serializers.py


# music_management/serializers.py
