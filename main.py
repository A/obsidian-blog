import time
from lib import builder
from lib.logger import log

log('Start a build')

tic = time.perf_counter()
builder.build()
toc = time.perf_counter()

log(f"The build has been finished in {toc - tic:0.4f} seconds")
