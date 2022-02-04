import time
from src.builder import Builder

tic = time.perf_counter()
timings = {}
Builder().build(timings)
toc = time.perf_counter()

print("")
print(f"{timings['posts_len']} posts have been rendered in {timings['posts']:0.4f} seconds")
print(f"{timings['pages_len']} pages have been rendered in {timings['pages']:0.4f} seconds")
print("")
print(f"The build has been finished in {toc - tic:0.4f} seconds\n")
