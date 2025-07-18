"""
Main body of code. Execute to start program.
"""

import json
import threading
import time
from app import App
from entities import Match

class NeonSslGui(object):
    def __init__(self):
        # Log file for the last session shall be emptied
        log_file = open("files/last_session_log.txt", "w")
        log_file.write("Last session started at: ")
        log_file.write(str(time.ctime(time.time())) + "\n")
        log_file.close()

        self.match = Match()
        self.app = App(self)

    def start(self):
        self.main_thread = threading.current_thread()

        self.update_thread = threading.Thread(target=self.update)
        self.update_thread.start()

        self.app.start()

    def update(self):
        # Send info to NeonFC
        pass

gui = NeonSslGui()
gui.start()