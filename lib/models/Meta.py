from datetime import datetime
from typing import Optional, TypedDict

Meta = TypedDict('Meta', {
  "title": Optional[str],
  "date": datetime,
  "layout": Optional[str],
}) 
