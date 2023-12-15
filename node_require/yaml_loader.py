# SPDX-License-Identifier: MIT

import typing as t
from pathlib import PurePath

from .require import Loader, one_of

__all__ = ("YAMLLoader", )


class YAMLLoader(Loader[t.Dict[str, t.Any]]):
    """A pre-made loader for YAML files."""

    extensions: t.ClassVar[t.List[str]] = [".yaml", ".yml"]

    def __init__(self) -> None:
        self.yaml = one_of(["yaml"])

    def load(self, path: PurePath) -> t.Dict[str, t.Any]:
        try:
            with open(path, "r") as fp:
                return self.yaml.loads(fp.read(), Loader = self.yaml.loader.FullLoader)
        except FileNotFoundError:
            raise ValueError(f"No such file: {path}") from None
