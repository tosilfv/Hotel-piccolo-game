"""
Music and sound effects for the game.
"""
import os
import pygame
from utils.constants import (SOUNDS_PATH)


class AudioManager:
    """
    Central manager for all game audio.

    Responsibilities:
        - Play background music (looped or selected times)
        - Stop or switch music tracks
        - Play short sound effects
        - Avoid reloading the same track unnecessarily
        - Maintain currently playing track state

    Attributes:
        currently_playing (str | None): Path to currently playing sound file
    """

    def __init__(self):
        # Initialize Pygame mixer
        pygame.mixer.init()
        self.currently_playing = None

    def play_music(self, filename: str, loops=-1) -> None:
        """
        Play a music track, looping if desired.

        Args:
            filename (str): Name of the music file
            loops (int): Number of loops (-1 = infinite)
        """
        music_file = os.path.join(SOUNDS_PATH, filename)

        if self.currently_playing != music_file:
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play(loops)
            self.currently_playing = music_file

    def stop_music(self) -> None:
        """
        Stop current music playback.
        """
        pygame.mixer.music.stop()
        self.currently_playing = None

    def play_sound(self, filename: str) -> None:
        """
        Play a short sound effect (non-blocking).

        Args:
            filename (str): Name of the sound file.
        """
        sound_file = os.path.join(SOUNDS_PATH, filename)

        sound = pygame.mixer.Sound(sound_file)
        sound.play()
