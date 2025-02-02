import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.restart_program()

    def restart_program(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen(['python', 'project.py', '/classes/Add_Manga_Window.py','/classes/Manga_App.py'], shell=True)

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print("Modifiche rilevate, riavvio del programma...")
            self.restart_program()

if __name__ == "__main__":
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
