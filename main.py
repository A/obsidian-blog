import time
from datetime import datetime
from lib import builder
from lib.logger import log

# TODO: Add partials support
# TODO: Recursive unwrapping support

log('Start a build')

tic = time.perf_counter()
builder.build()
toc = time.perf_counter()

log(f"The build has been finished in {toc - tic:0.4f} seconds")
