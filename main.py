import time
from obsidian_blog.builder import Builder
from obsidian_blog.logger import log

tic = time.perf_counter()
timings = {}
Builder().build(timings)
toc = time.perf_counter()

log(f"\nAll posts have been rendered in {timings['posts']:0.4f} seconds")
log(f"All pages have been rendered in {timings['pages']:0.4f} seconds")
log(f"The build has been finished in {toc - tic:0.4f} seconds\n")
