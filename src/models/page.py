class PageModel:
  def __init__(self, filename = None, meta=None, content=""):
    self.filename = filename
    self.meta = meta
    self.content =  content
    self.entities = []

  def __eq__(self, other): 
    if not isinstance(other, PageModel):
      return NotImplemented
    return self.filename == other.filename
