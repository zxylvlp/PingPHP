import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from helper import *


class FileChangeEventHandler(FileSystemEventHandler):
    def on_moved(self, event):
        super(FileChangeEventHandler, self).on_moved(event)

    def on_created(self, event):
        super(FileChangeEventHandler, self).on_created(event)
        if not event.src_path_ in filesNoCache():
            return
        #doTranslate(event.src_path_)
        transFilesNoExit()

    def on_deleted(self, event):
        super(FileChangeEventHandler, self).on_deleted(event)

    def on_modified(self, event):
        super(FileChangeEventHandler, self).on_modified(event)
        self.on_created(event)

    def dispatch(self, event):
        if event.is_directory:
            return
        event.src_path_ = event.src_path.lstrip('./')
        if hasattr(event, 'dest_path'):
            event.dest_path_ = event.dest_path.lstrip('./')
        super(FileChangeEventHandler, self).dispatch(event)


def initMonitor():
    eventHandler = FileChangeEventHandler()
    observer = Observer()
    observer.schedule(eventHandler, '.', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
