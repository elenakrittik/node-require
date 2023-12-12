# SPDX-License-Identifier: LGPL-3.0-only

import os
from pathlib import PurePath
import sys
from .require import Loader
from types import ModuleType
import importlib


class ModuleLoader(Loader[ModuleType]):
    """A pre-made loader for Python modules. Enabled by default."""

    def __init__(self) -> None:
        self.extensions = [".py"]

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
