import os
import sys
from .req_impl import Loader

class ModuleLoader(Loader):
    """
    Builtin loader for Python modules
    """
    def __init__(self):
        self.extensions = ['.py']
        self.deps = []
        self.optional_deps = {}
    
    def load(self, path: str, file: str):
        r = None
        old = sys.path.copy()
        sys.path = [os.path.abspath(path)]
        try:
            r = __import__(file[:-3])
        except ModuleNotFoundError:
            sys.path = old
            raise ValueError(f"No such module: {file}") from None
        sys.path = old
        return r

loader = ModuleLoader