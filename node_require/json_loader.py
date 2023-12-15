# SPDX-License-Identifier: MIT

import typing as t
from pathlib import PurePath

from .require import Loader, one_of

__all__ = ("JSONLoader", )


class JSONLoader(Loader[t.Dict[str, t.Any]]):
    """A pre-made loader for JSON files. Enabled by default.

    Can utilize ``orjson`` or ``ujson`` if available.
    """

    extensions: t.ClassVar[t.List[str]] = [".json"]

    def __init__(self) -> None:
        self.json = one_of(["orjson", "ujson", "json"])

    def load(self, path: PurePath) -> t.Dict[str, t.Any]:
        try:
            with open(path, "rb") as fp:
                return self.json.loads(fp.read())
        except FileNotFoundError:
            raise ValueError(f"No such file: {path}") from None
