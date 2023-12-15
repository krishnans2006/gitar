from gitar.models import Note


class Chord:
    def __init__(self, name: str):
        self.name = name

        self.notes: list[Note] = []

    def initialize(self, notes: list[Note]):
        self.notes = notes

    def play(self):
        for note in self.notes:
            note.press()

    def unplay(self, next_chord: "Chord"):
        for note in self.notes:
            if note not in next_chord.notes:
                note.release()
