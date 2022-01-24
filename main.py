import time
from src.builder import Builder
from src.logger import log

tic = time.perf_counter()
timings = {}
Builder().build(timings)
toc = time.perf_counter()

print(f"\nAll posts have been rendered in {timings['posts']:0.4f} seconds")
print(f"All pages have been rendered in {timings['pages']:0.4f} seconds")
print(f"The build has been finished in {toc - tic:0.4f} seconds\n")
