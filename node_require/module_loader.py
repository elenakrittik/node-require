# SPDX-License-Identifier: MIT

import importlib
import os
import sys
import typing as t
from pathlib import PurePath
from types import ModuleType

from .require import Loader

__all__ = ("ModuleLoader", )


class ModuleLoader(Loader[ModuleType]):
    """A pre-made loader for Python modules. Enabled by default."""

    extensions: t.ClassVar[t.List[str]] = [".py"]

    def load(self, path: PurePath) -> ModuleType:
        old = sys.path.copy()
        sys.path = [os.path.abspath(path)]

        try:
            module = importlib.import_module(path.stem)
        except ModuleNotFoundError:
            raise ValueError(f"No module at {path}") from None
        finally:
            sys.path = old

        return module
