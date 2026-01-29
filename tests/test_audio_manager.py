import os
import pytest
from unittest.mock import patch, MagicMock
from game_objects.audio_manager import AudioManager

class TestAudioManager:
    @patch("pygame.mixer.music")
    @patch("pygame.mixer.init")
    def test_play_music_loads_and_plays(self, mock_init, mock_music):
        audio_manager = AudioManager()
        
        # Alkuperäisenä ei soiteta mitään
        assert audio_manager.currently_playing is None

        # Kutsu play_music
        audio_manager.play_music("music_yard.wav", loops=2)

        # Tarkista, että music.load ja music.play kutsuttiin oikein
        mock_music.load.assert_called_once()
        mock_music.play.assert_called_once_with(2)
        # currently_playing päivittyi
        assert audio_manager.currently_playing is not None
        assert os.path.basename(audio_manager.currently_playing) == "music_yard.wav"

        # Jos kutsutaan uudestaan samalla tiedostolla, load ei pitäisi tapahtua uudestaan
        mock_music.reset_mock()
        audio_manager.play_music("music_yard.wav")
        mock_music.load.assert_not_called()
        mock_music.play.assert_not_called()  # Jos haluat, voit päättää soittako uudestaan vai ei

    @patch("pygame.mixer.music")
    @patch("pygame.mixer.init")
    def test_stop_music(self, mock_init, mock_music):
        audio_manager = AudioManager()
        audio_manager.currently_playing = "somefile.wav"

        audio_manager.stop_music()

        mock_music.stop.assert_called_once()
        assert audio_manager.currently_playing is None
