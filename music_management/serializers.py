from .models import Song, Playlist
from rest_framework import serializers


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'youtube_link', 'music_link']


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name','songs']
