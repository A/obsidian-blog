import os
from src.dataclasses.config_data import ConfigData
from src.tasks.builder import BuilderTask
from src.lib.watcher import Watcher
from watchdog.events import FileSystemEventHandler


class WatcherTask:
    def __init__(self, config: ConfigData) -> None:
        ignore_dir = os.path.abspath(config.dest_dir)
        self.start_watcher(ignore_dir=ignore_dir)

    @staticmethod
    async def run(config: ConfigData):
        WatcherTask(config)

    def callback(self):
        BuilderTask.run()

    def start_watcher(self, ignore_dir):
        Handler = self.create_handler(ignore_dir, self.callback)
        self.watcher = Watcher(Handler, path='.')
        self.watcher.run()

    def create_handler(self, ignore_dir, callback):
        
        class Handler(FileSystemEventHandler):
            @staticmethod
            def on_any_event(event):
                is_ignored = event.src_path.startswith(ignore_dir)
                if is_ignored: return

                print(f'File changed: <{event.event_type}> {event.src_path}')
                callback()

        return Handler
