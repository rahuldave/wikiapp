import importlib.metadata

print(">>>", __name__, __package__)
__version__ = importlib.metadata.version(__name__ or __package__)
