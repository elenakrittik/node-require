.. SPDX-License-Identifier: MIT

.. currentmodule:: node_require

Quickstart
==========

To get started, let's create a simple program that
``require()``\s a module, which, in turn, ``require()``\s
a JSON file and then prints it's contents (a
"Hello, World" string).

First, create `data/data.json`:

.. code-block:: json

    {
        "message": "Hello, World!"
    }

Then create `main.py` (as the name suggests, the
entry point for our program):

.. code-block:: python

    from typing import TypedDict

    from node_require import require

    class MyData(TypedDict):
        message: str

    # Note that `require()` expects path to be relative
    # to run root, like many built-in Python functions do.
    data: MyData = require("modules/my_module.py").data

    print(data["message"])

Now create `modules/my_module.py`:

.. code-block:: python

    from node_require import require

    data = require("data/data.json")

And this is it! You can run `python main.py` and see
a "Hello, World!" message. Also, do note that this is
an overexaggerated example (you can just ``print("Hello, World")``
for the same result), but it shows the basics.
