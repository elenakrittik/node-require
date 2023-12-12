# SPDX-License-Identifier: LGPL-3.0-only

from pathlib import PurePath
import typing as t
from .require import Loader, one_of


class TOMLLoader(Loader[t.Dict[str, t.Any]]):
    """A pre-made loader for TOML files."""

    def __init__(self) -> None:
        self.toml = one_of(["toml"])
        self.extensions = [".toml"]

    def load(self, path: PurePath) -> t.Dict[str, t.Any]:
        try:
            with open(path, "r") as fp:
                return self.toml.loads(fp.read())
        except FileNotFoundError:
            raise ValueError(f"No such file: {path}") from None
