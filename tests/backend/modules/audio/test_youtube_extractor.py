import unittest
from unittest.mock import patch, MagicMock
from src.backend.modules.audio.youtube_extractor import extract_audio_from_youtube

class TestYoutubeExtractor(unittest.TestCase):

    @patch('src.backend.modules.audio.youtube_extractor.YouTube')
    def test_extract_audio_from_youtube_success(self, mock_youtube):
        mock_stream = MagicMock()
        mock_stream.download.return_value = '/path/to/downloaded/audio.mp4'
        mock_youtube.return_value.streams.filter.return_value.first.return_value = mock_stream

        result = extract_audio_from_youtube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        
        self.assertEqual(result, '/path/to/downloaded/audio.mp4')
        mock_youtube.assert_called_once_with('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        mock_youtube.return_value.streams.filter.assert_called_once_with(only_audio=True)
        mock_stream.download.assert_called_once()

    @patch('src.backend.modules.audio.youtube_extractor.YouTube')
    def test_extract_audio_from_youtube_no_audio_stream(self, mock_youtube):
        mock_youtube.return_value.streams.filter.return_value.first.return_value = None

        with self.assertRaises(ValueError) as context:
            extract_audio_from_youtube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        
        self.assertEqual(str(context.exception), "No audio stream found for the given YouTube video.")

    @patch('src.backend.modules.audio.youtube_extractor.YouTube')
    def test_extract_audio_from_youtube_download_error(self, mock_youtube):
        mock_stream = MagicMock()
        mock_stream.download.side_effect = Exception("Download failed")
        mock_youtube.return_value.streams.filter.return_value.first.return_value = mock_stream

        with self.assertRaises(Exception) as context:
            extract_audio_from_youtube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        
        self.assertEqual(str(context.exception), "Download failed")

    def test_extract_audio_from_youtube_invalid_url(self):
        with self.assertRaises(ValueError) as context:
            extract_audio_from_youtube('not_a_valid_url')
        
        self.assertEqual(str(context.exception), "Invalid YouTube URL provided.")

    @patch('src.backend.modules.audio.youtube_extractor.YouTube')
    def test_extract_audio_from_youtube_connection_error(self, mock_youtube):
        mock_youtube.side_effect = Exception("Connection error")

        with self.assertRaises(Exception) as context:
            extract_audio_from_youtube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        
        self.assertEqual(str(context.exception), "Connection error")
