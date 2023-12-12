# SPDX-License-Identifier: LGPL-3.0-only

from pathlib import PurePath
import typing as t
from .require import Loader, one_of


class BSONLoader(Loader[t.Dict[str, t.Any]]):
    """A pre-made loader for BSON files that outputs a dictionary."""

    def __init__(self) -> None:
        self.bson = one_of(["bson"])
        self.extensions = [".bson"]

    def load(self, path: PurePath) -> t.Dict[str, t.Any]:
        try:
            with open(path, "rb") as fp:
                return self.bson.loads(fp.read())
        except FileNotFoundError:
            raise ValueError(f"No such file: {path}") from None
