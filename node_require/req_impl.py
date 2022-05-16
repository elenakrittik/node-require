import os
import re
import warnings
import typing as T
import importlib as ilib
from pip._internal.commands.show import search_packages_info as spi

_almost_any: str = "[a-zA-Z0-9_\\./\\$&;!-#@~`\\^%\\{\\}\\[\\]\\(\\)\\+ ]"
_l: str = "[a-zA-Z0-9_\\$&;!-#@~`\\^%\\{\\}\\[\\]\\(\\) ]"
QUERY: re.Pattern = re.compile(f"({_almost_any})+({_l})*\.({_almost_any})+")

T.Module = T.TypeVar("module", os.__class__, os.__class__)

loaders = {}

pkg = None
for entry in spi(['node_require']):
    pkg = entry
    break

class ExtNotSupported(Exception):
    """
    Exception that is raised when you trying to load unsupported file extension
    """

class LibRequired(Exception):
    """
    Exception that is raised when you trying to load extension that is supported, but dependencies for it are not resolved
    """

class Loader:
    """
    Abstract base class (ABC) for all loaders.
    """
    extensions: T.List[str]
    deps: T.List[str]
    optional_deps: T.Dict[str, str]
    
    def load(self, path: str, file: str) -> T.Any:
        """
        A function to be overridden by developer.
        """
        raise NotImplementedError

def require(q: str) -> T.Any:
    """
    Like a Node's ``require()``
    
    Parameters
    ----------
    q: str
        The query, e.g., "../mymodule.py" or "./config.json"
    
    Returns
    -------
    Any
        The type depends on file you required. For example, if you required a Python file, it will return a Python module (if .py loader was not overridden)
    """
    # some checking
    if not QUERY.match(q):
        warnings.warn("It looks like you given an invalid path to file.")
    path, file = _parse(q)
    piece = _import(path, file)
    return piece

def _parse(q: str) -> T.Tuple[str, str]:
    newpart = False
    parts = []
    s = ""
    for x in q:
        if newpart:
            newpart = False
            parts.append(s)
            s = ""
        s += x
        if x == '/':
            newpart = True
    parts.append(s)
    file = parts.pop(len(parts) - 1)
    path = ''.join(parts)
    return (path, file)

def _import(path, file) -> T.Any:
    for x in list(loaders.keys()):
        if file.endswith(x):
            r = loaders[x].load(path, file)
            return r
    raise ExtNotSupported("The file you required ({file}) have unsupported extension")

def use(loader: Loader) -> None:
    """
    Register loader.
    
    Parameters
    ----------
    loader: Loader
       The loader
    """
    l = loader()
    for ext in l.extensions:
        loaders[ext] = l

def one_of(q: T.List[str]) -> T.Module:
    """
    Tries to import one of requested modules.
    """
    for module in q:
        try:
            return __import__(module)
        except ImportError:
            continue
    raise LibRequired("Please install one of the following libraries to use this loader: " + ", ".join(q))

def _one_of(q: T.List[str]) -> T.Module:
    """
    Silent version of ``one_of``. **Internal use only!**
    """
    try:
        return one_of(q)
    except LibRequired:
        return None

for loader_file in os.listdir(pkg.location + "/node_require"):
    if loader_file.endswith('_loader.py'):
        use(ilib.import_module(f".{loader_file[:-3]}", package="node_require").loader)
