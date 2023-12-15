import math
import time
from typing import TYPE_CHECKING

import pause

if TYPE_CHECKING:
    from gitar.models.song import Song


class Strummer:
    def __init__(self, song: Song):
        self.song = song
        self.delay = 60 / self.song.tempo  # bpm -> s/b

        self.status = "stopped"

    def strum(self):
        print("strum")

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

            self.strum()

            time.sleep(self.delay)
