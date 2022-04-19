import os
import typing as T
from .req_impl import Loader, _one_of, LibRequired

class TomlLoader(Loader):
    """
    Builtin loader for Toml files
    """
    def __init__(self):
        self.toml = _one_of(["toml"])
        self.extensions = ['.toml']
        self.deps = ['toml']
        self.optional_deps = {}
    
    def load(self, path: str, file: str) -> T.Dict[str, T.Any]:
        if not self.toml:
            raise LibRequired("The toml library is required to load .toml files") from None
        try:
            with open(os.path.abspath(path) + '/' + file, 'r') as fp:
                return self.toml.loads(fp.read())
        except FileNotFoundError:
            raise ValueError(f"No such file: {file}") from None

loader = TomlLoader