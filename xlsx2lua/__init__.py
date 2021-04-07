__version__ = "1.0.0.0"

from .environment import Environment

def parse(*args):
    return Environment(*args)

