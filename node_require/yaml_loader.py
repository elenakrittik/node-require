# SPDX-License-Identifier: LGPL-3.0-only

from pathlib import PurePath
import typing as t
from .require import Loader, one_of


class YAMLLoader(Loader[t.Dict[str, t.Any]]):
    """A pre-made loader for YAML files."""

    def __init__(self) -> None:
        self.yaml = one_of(["yaml"])
        self.extensions = [".yaml", ".yml"]

    def load(self, path: PurePath) -> t.Dict[str, t.Any]:
        try:
            with open(path, "r") as fp:
                return self.yaml.loads(fp.read(), Loader = self.yaml.loader.FullLoader)
        except FileNotFoundError:
            raise ValueError(f"No such file: {path}") from None
