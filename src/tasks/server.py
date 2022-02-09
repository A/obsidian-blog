from src.dataclasses.config_data import ConfigData
from src.lib.http_server import HTTPServer


class ServerTask:
    def __init__(self, config=ConfigData):
        self.start_server(directory=config.dest_dir, port=config.port)

    def start_server(self, directory, port):
        HTTPServer(port=port, directory=directory)

    @staticmethod
    def run(config: ConfigData):
        ServerTask(config)
