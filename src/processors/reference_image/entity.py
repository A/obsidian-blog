from src.processors.reference_image import consts as c

class ReferenceImageEntity:
  parser_key = c.REFERENCE_IMAGE_PARSER_KEY

  def __init__(self, placeholder, alt, filename, key):
    self.placeholder = placeholder
    self.alt = alt
    self.key = key
    self.filename = filename
