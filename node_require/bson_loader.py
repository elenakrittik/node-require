import os
import typing as T
from .req_impl import Loader, _one_of, LibRequired

class BSONLoader(Loader):
    """
    Builtin loader for BSON files
    """
    def __init__(self):
        self.bson = _one_of(["bson"])
        self.extensions = ['.bson']
        self.deps = ["bson"]
        self.optional_deps = {}
    
    def load(self, path: str, file: str) -> T.Dict[str, T.Any]:
        if not self.bson:
            raise LibRequired("The bson library is required to load .bson files") from None
        try:
            with open(os.path.abspath(path) + '/' + file, 'rb') as fp:
                return self.bson.loads(fp.read())
        except FileNotFoundError:
            raise ValueError(f"No such file: {file}") from None

loader = BSONLoader