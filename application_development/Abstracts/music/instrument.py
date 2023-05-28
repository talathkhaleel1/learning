

from abc import ABC


class Instrument:

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def play(self, music_tune : str):
        self.music_tune = music_tune
        return self.music_tune

