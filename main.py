from datetime import datetime
from lib import builder

# TODO: Verbose logging
# TODO: Add partials support

print('Start a build', datetime.now())

builder.build()

print("The build is finished:", datetime.now())
