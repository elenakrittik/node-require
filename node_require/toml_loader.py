# SPDX-License-Identifier: MIT

import typing as t
from pathlib import PurePath

from .require import Loader, one_of

__all__ = ("TOMLLoader", )


class TOMLLoader(Loader[t.Dict[str, t.Any]]):
    """A pre-made loader for TOML files."""

    extensions: t.ClassVar[t.List[str]] = [".toml"]

    def __init__(self) -> None:
        self.toml = one_of(["toml"])

    def load(self, path: PurePath) -> t.Dict[str, t.Any]:
        try:
            with open(path, "r") as fp:
                return self.toml.loads(fp.read())
        except FileNotFoundError:
            raise ValueError(f"No such file: {path}") from None
