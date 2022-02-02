class InlineImageRenderer:

  def render(self, content, entity):
    rendered_image = f"[{entity.alt}]({entity.filename})"
    return content.replace(entity.placeholder, rendered_image)
