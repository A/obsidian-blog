from src.processors.inline_image import consts as c

class InlineImageEntity:
  parser_key = c.INLINE_IMAGE_PARSER_KEY

  def __init__(self, placeholder, alt, filename):
    self.placeholder = placeholder
    self.alt = alt
    self.filename = filename

