# SPDX-License-Identifier: LGPL-3.0-only

from __future__ import annotations
from abc import ABC, abstractmethod
import typing as t
from pathlib import PurePath
import importlib

if t.TYPE_CHECKING:
    import types

from .exceptions import ExtNotSupported, LibRequired
from .json_loader import JSONLoader

T = t.TypeVar("T")

loaders: t.Dict[str, Loader[t.Any]] = {}


class Loader(ABC, t.Generic[T]):
    """Abstract base class (ABC) for all loaders.

    Attributes
    ----------
    extensions: :class:`list`[:class:`str`]
        List of file extensions this loader supports.
    """

    extensions: t.List[str]

    @abstractmethod
    def load(self, path: PurePath) -> T:
        """Call to load a file with respective extension."""


def require(query: str) -> t.Any:
    """Request a file, similar to Node.js' ``require()``.

    Parameters
    ----------
    query: str
        The query, e.g., "../mymodule.py" or "./config.json"

    Returns
    -------
    Any
        The type depends on the file you reqested. For example,
        if you required a Python file, this will be a Python
        module (if .py loader was not overridden).
    """
    path = PurePath(query)

    try:
        return loaders["".join(path.suffixes)].load(path)
    except KeyError:
        raise ExtNotSupported(f"{path} has an unsupported extension") from None


def use(loader: Loader[t.Any]) -> None:
    """Register a loader.

    Parameters
    ----------
    loader: Loader
       The loader.
    """
    for ext in loader.extensions:
        loaders[ext] = loader


def one_of(modules: t.List[str]) -> types.ModuleType:
    """Try to import one of requested modules."""
    for module in modules:
        try:
            return importlib.import_module(module)
        except ImportError:  # noqa: PERF203
            continue
    raise LibRequired(
        f"Please install one of the following libraries to use this loader: {', '.join(modules)}",
    )


use(JSONLoader())
