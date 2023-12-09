from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gitar.models.song import Song


class Strummer:
    def __init__(self, song: Song):
        self.song = song
