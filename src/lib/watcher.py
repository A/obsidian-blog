import time
from watchdog.observers import Observer


class Watcher:
    def __init__(self, Handler, path):
        self.observer = Observer()
        self.Handler = Handler
        self.path = path

    def run(self):
        event_handler = self.Handler()
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()
        self.observer.join()
