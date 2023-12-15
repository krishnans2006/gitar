import math
import time
from typing import TYPE_CHECKING

import pause

from gitar.models import Chord

if TYPE_CHECKING:
    from gitar.models.song import Song


class ChordPlayer:
    def __init__(self, song: Song):
        self.song = song
        self.delay = 60 / self.song.tempo  # bpm -> s/b

        self.chords: list[Chord] = []
        self.current_chord: int = -1

        self.status = "stopped"

    def initialize(self, chords):
        self.chords = chords
        self.current_chord = 0

    def play(self, actions):
        while True:
            action = actions.get()
            if action == "pause":
                self.status = "paused"
            elif action == "resume":
                self.status = "resuming"
            elif action == "stop":
                self.status = "stopped"
                break

            if self.status == "paused":
                time.sleep(0.1)
                continue
            elif self.status == "resuming":
                now = time.time()
                resume_time = math.ceil(now + 1)
                pause.until(resume_time)
                self.status = "playing"
                continue

            self.chords[self.current_chord].play()

            time.sleep(self.delay)
