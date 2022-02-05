import time
from src.builder import Builder
from src.dataclasses.config_data import ConfigData

tic = time.perf_counter()
timings = {}

config = ConfigData()
Builder().build(
  timings,
  config=config
)
toc = time.perf_counter()

print("---\n")
print(f"The build has been finished in {toc - tic:0.4f} seconds\n")
