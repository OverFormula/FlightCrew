
class TenetRegistry:
  registry = []

  @classmethod
  def add_tenet(cls, tenet):
    cls.registry.append(tenet)

  @classmethod
  def get_tenets(cls):
    return cls.registry
