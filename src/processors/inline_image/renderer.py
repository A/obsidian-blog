from src.processors.inline_image.entity import InlineImageEntity


class InlineImageRenderer:

  def render(self, content, entity: InlineImageEntity):
    rendered_image = f"[{entity.alt}]({entity.filename})"
    return content.replace(entity.placeholder, rendered_image)
