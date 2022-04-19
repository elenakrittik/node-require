import os
import typing as T
from .req_impl import Loader, _one_of

class JSONLoader(Loader):
    """
    Builtin loader for JSON files
    """
    def __init__(self):
        self.json = _one_of(["orjson", "ujson", "json"])
        self.extensions = ['.json']
        self.deps = []
        self.optional_deps = {
            "orjson": "Speedup",
            "ujson": "Alternative for orjson"
        }
    
    def load(self, path: str, file: str) -> T.Dict[str, T.Any]:
        try:
            with open(os.path.abspath(path) + '/' + file, 'rb') as fp:
                return self.json.loads(fp.read())
        except FileNotFoundError:
            raise ValueError(f"No such file: {file}") from None

loader = JSONLoader