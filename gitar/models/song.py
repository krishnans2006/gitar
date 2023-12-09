from threading import Thread
from queue import Queue

from gitar.models import ChordPlayer, Strummer


class Song:
    def __init__(self, name, artist=None, album=None, year=None, genre=None, tempo=None):
        self.name = name
        self.artist = artist
        self.album = album
        self.year = year
        self.genre = genre
        self.tempo = tempo

        self.chord = None
        self.chord_thread = None
        self.chord_actions = Queue()

        self.strum = None
        self.strum_thread = None
        self.strum_actions = Queue()

    def initialize(self):
        self.chord = ChordPlayer
        self.strum = Strummer

    @property
    def is_playing(self):
        return self.chord_thread.is_alive() or self.strum_thread.is_alive()

    def start(self):
        self.chord_thread = Thread(target=self.chord.play, args=(self.chord_actions,))
        self.strum_thread = Thread(target=self.strum.play, args=(self.strum_actions,))

        self.chord_thread.start()
        self.strum_thread.start()

    def pause(self, thread=None):
        if thread == "chord" or thread is None:
            self.chord_actions.put("pause")
        elif thread == "strum" or thread is None:
            self.strum_actions.put("pause")

    def resume(self, thread=None):
        if thread == "chord" or thread is None:
            self.chord_actions.put("resume")
        elif thread == "strum" or thread is None:
            self.strum_actions.put("resume")

    def stop(self, thread=None):
        if thread == "chord" or thread is None:
            self.chord_actions.put("stop")
        elif thread == "strum" or thread is None:
            self.strum_actions.put("stop")

        self.chord_thread.join()
        self.strum_thread.join()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Song name={self.name} artist={self.artist} album={self.album} year={self.year} genre={self.genre}>"
