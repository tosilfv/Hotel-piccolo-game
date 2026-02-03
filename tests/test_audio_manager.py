"""Unit tests for AudioManager game object"""
import os
from unittest.mock import patch, MagicMock
from game_objects.audio_manager import AudioManager


class TestAudioManager:
    """Test AudioManager class"""

    @patch("game_objects.audio_manager.pygame.mixer.init")
    @patch("game_objects.audio_manager.pygame.mixer.music")
    def test_play_music_loads_and_plays(self, mock_music, mock_init):
        # Setup
        audio_manager = AudioManager()
        assert audio_manager.currently_playing is None

        # Action
        audio_manager.play_music("music_yard.wav", loops=2)

        # Assert
        mock_music.load.assert_called_once()
        mock_music.play.assert_called_once_with(2)
        assert audio_manager.currently_playing is not None
        assert os.path.basename(audio_manager.currently_playing) == "music_yard.wav"

        # Action: call again with same file
        mock_music.reset_mock()
        audio_manager.play_music("music_yard.wav")

        # Assert: load and play not called again
        mock_music.load.assert_not_called()
        mock_music.play.assert_not_called()

    @patch("game_objects.audio_manager.pygame.mixer.init")
    @patch("game_objects.audio_manager.pygame.mixer.music")
    def test_stop_music(self, mock_music, mock_init):
        # Setup
        audio_manager = AudioManager()
        audio_manager.currently_playing = "somefile.wav"

        # Action
        audio_manager.stop_music()

        # Assert
        mock_music.stop.assert_called_once()
        assert audio_manager.currently_playing is None

    @patch("game_objects.audio_manager.pygame.mixer.init")
    @patch("game_objects.audio_manager.pygame.mixer.Sound")
    def test_play_sound_plays_with_volume(self, mock_sound_class, mock_init):
        # Setup
        mock_sound = MagicMock()
        mock_sound_class.return_value = mock_sound
        audio_manager = AudioManager(sound_volume=0.5)

        # Action
        audio_manager.play_sound("click.wav")

        # Assert
        mock_sound_class.assert_called_once()
        mock_sound.set_volume.assert_called_once_with(0.5)
        mock_sound.play.assert_called_once()
