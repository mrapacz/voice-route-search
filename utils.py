import os
from threading import Thread


def run_dogg():
    def play_dogg():
        os.system("afplay ~/Downloads/dogg.m4a")

    Thread(target=play_dogg).start()
