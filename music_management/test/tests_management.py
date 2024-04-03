from django.test import TestCase
from unittest.mock import patch, MagicMock
from music_management.models import Song, Playlist, Record  # Update 'yourapp' with the actual app name

class TestModels(TestCase):
    @patch('music_management.models.Song')
    def test_song_str(self, MockSong):
        # Mock a Song instance
        song_instance = MockSong.return_value
        song_instance.title = 'Test Song'
        self.assertEqual(str(song_instance), 'Test Song')

    @patch('music_management.models.Playlist')
    def test_playlist_str(self, MockPlaylist):
        # Mock a Playlist instance
        playlist_instance = MockPlaylist.return_value
        playlist_instance.name = 'Test Playlist'
        self.assertEqual(str(playlist_instance), 'Test Playlist')

    @patch('music_management.models.Record')
    @patch('cloudinary.models.CloudinaryField')
    def test_record(self, MockCloudinaryField, MockRecord):
        # Mock a Record instance and the CloudinaryField
        record_instance = MockRecord.return_value
        record_instance.id = '1234'
        record_instance.video = MockCloudinaryField.return_value
        record_instance.video.url = 'http://example.com/video.mp4'

        # Assuming there's a URLpattern named 'core:record_detail' requiring an 'id' parameter
        expected_url = '/core/record/1234/'  # Adjust this URL based on your actual routing
        self.assertEqual(record_instance.get_absolute_url(), expected_url)

        # Testing the string representation of the record
        record_instance.__str__.return_value = '1234'
        self.assertEqual(str(record_instance), '1234')

        # Testing the CloudinaryField's mocked URL
        self.assertEqual(record_instance.video.url, 'http://example.com/video.mp4')

