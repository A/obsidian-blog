from abc import ABC, abstractmethod
from src.entities.page_data import PageData

class EntityInterface(ABC):
  """Basic entity interface"""

  @staticmethod
  @abstractmethod
  def get_all(data: PageData):
    """parse all reference image entities from a given page model"""
    pass
  
  @abstractmethod
  def render(self, data: PageData):
    pass
