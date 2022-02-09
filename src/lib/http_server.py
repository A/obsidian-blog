import http.server
import socketserver


class HTTPServer:
    def __init__(self, port: int, directory: str) -> None:
        self.port = port
        self.directory = directory
        self.start()

    def start(self):
        with socketserver.TCPServer(
            ('', self.port), self.create_handler()
        ) as httpd:
            print(f'Start server at {self.port} port')
            httpd.serve_forever()

    def create_handler(self):
        def _init(self, *args, **kwargs):
            return http.server.SimpleHTTPRequestHandler.__init__(
                self, *args, directory=self.directory, **kwargs
            )

        return type(
            f'HandlerFrom<{self.directory}>',
            (http.server.SimpleHTTPRequestHandler,),
            {'__init__': _init, 'directory': self.directory},
        )
