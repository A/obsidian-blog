import asyncio
from threading import Thread
from docopt import docopt
from src.config import config
from src.tasks.builder import BuilderTask
from src.tasks.server import ServerTask
from src.tasks.watcher import WatcherTask


doc = """obsidian-blog

Static site generator for obsidian.md notes.

Usage:
  obsidian-blog [-d] [-w] [-s] [--port <number>] [--title <string>] [--posts_dir <directory>] [--pages_dir <directory>]

Options:
  -h --help                     Show this screen.
  -w --watch                    Enable watcher
  -s --serve                    Enable web-server
  -p --port=<number>            Web-server port [default: 4200]
  -d --drafts                   Render draft pages and posts

  --title=<string>              Blog title [default: My Blog]

  --version             Show version.
"""


def main():
    args = docopt(doc, version='0.0.0')
    serve = args['--serve']
    watch = args['--watch']

    config.override(
        {
            'port': int(args['--port']),
            'blog_title': args['--title'],
            'drafts': args['--drafts'],
        }
    )
    config.load_dotenv()

    BuilderTask.run(config)

    threads = []
    if serve:
        t = Thread(target=ServerTask.run, args=(config,))
        threads.append(t)

    if watch:
        t = Thread(target=WatcherTask.run, args=(config,))
        threads.append(t)

    for t in threads:
        t.start()


if __name__ == '__main__':
    main()
