import asyncio
from docopt import docopt
from src.dataclasses.config_data import ConfigData
from src.tasks.builder import BuilderTask
from src.tasks.server import ServerTask
from src.tasks.watcher import WatcherTask


doc = """obsidian-blog

Static site generator for obsidian.md notes.

Usage:
  obsidian-blog [-w] [-s] [--port <number>] [--title <string>] [--posts_dir <directory>] [--pages_dir <directory>]

Options:
  -h --help                     Show this screen.
  -w --watch                    Enable watcher
  -s --serve                    Enable web-server
  -p --port=<number>            Web-server port [default: 4200]

  --title=<string>              Blog title [default: My Blog]
  --posts_dir=<directory>       Posts directory to parse [default: Posts]
  --pages_dir=<directory>       Pages directory to parse [default: Pages]

  --version             Show version.
"""


def cli():
    args = docopt(doc, version='0.0.0')
    serve = args['--serve']
    watch = args['--watch']

    config = ConfigData()
    config.override(
        {
            'port': int(args['--port']),
            'blog_title': args['--title'],
            'posts_dir': args['--posts_dir'],
            'pages_dir': args['--pages_dir'],
        }
    )
    config.load_dotenv()

    BuilderTask.run(config)

    if serve:
        asyncio.run(ServerTask.run(config))

    if watch:
        asyncio.run(WatcherTask.run(config))
