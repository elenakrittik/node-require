# SPDX-License-Identifier: LGPL-3.0-only

from pathlib import PurePath
import typing as t
from .require import Loader, one_of


class JSONLoader(Loader[t.Dict[str, t.Any]]):
    """A pre-made loader for JSON files. Enabled by default.

    Can utilize ``orjson`` or ``ujson`` if available.
    """

    def __init__(self) -> None:
        self.json = one_of(["orjson", "ujson", "json"])
        self.extensions = [".json"]

    def load(self, path: PurePath) -> t.Dict[str, t.Any]:
        try:
            with open(path, "rb") as fp:
                return self.json.loads(fp.read())
        except FileNotFoundError:
            raise ValueError(f"No such file: {path}") from None
