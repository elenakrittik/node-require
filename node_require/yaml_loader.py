import os
import typing as T
from .req_impl import Loader, _one_of, LibRequired

class YAMLLoader(Loader):
    """
    Builtin loader for YAML files
    """
    def __init__(self):
        self.yaml = _one_of(["yaml"])
        self.extensions = ['.yaml', '.yml']
        self.deps = ['yaml']
        self.optional_deps = {}
    
    def load(self, path: str, file: str) -> T.Dict[str, T.Any]:
        if not self.yaml:
            raise LibRequired("The yaml library is required to load .yaml files") from None
        try:
            with open(os.path.abspath(path) + '/' + file, 'r') as fp:
                return self.yaml.loads(fp.read(), Loader=self.yaml.loader.FullLoader)
        except FileNotFoundError:
            raise ValueError(f"No such file: {file}") from None

loader = YAMLLoader