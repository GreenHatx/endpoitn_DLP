from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import winHandler

class Watcher:
    def __init__(self, path):
        self.observer = Observer()
        self.path = path

    def run(self):
        event_handler = winHandler.Handler()
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()

