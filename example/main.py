# SPDX-License-Identifier: MIT

from typing import TypedDict

from node_require import require


class MyData(TypedDict):
    message: str


data: MyData = require("modules/my_module.py").data

print(data["message"])
