# SPDX-License-Identifier: MIT

import typing as t
from pathlib import PurePath

from .require import Loader, one_of

__all__ = ("BSONLoader", )


class BSONLoader(Loader[t.Dict[str, t.Any]]):
    """A pre-made loader for BSON files that outputs a dictionary."""

    extensions: t.ClassVar[t.List[str]] = [".bson"]

    def __init__(self) -> None:
        self.bson = one_of(["bson"])

    def load(self, path: PurePath) -> t.Dict[str, t.Any]:
        try:
            with open(path, "rb") as fp:
                return self.bson.loads(fp.read())
        except FileNotFoundError:
            raise ValueError(f"No such file: {path}") from None
