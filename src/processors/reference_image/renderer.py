from src.processors.reference_image.entity import ReferenceImageEntity


class ReferenceImageRenderer:

  def render(self, content, entity: ReferenceImageEntity):
    rendered_image = f"[{entity.alt}]({entity.filename})"
    return content.replace(entity.placeholder, rendered_image)
