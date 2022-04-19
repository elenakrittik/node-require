node-require
=======

Like Node.js's require(), but with more supported file formats

Features
--------

- Importing modules from higher folders
- Loading JSON, Toml, YAMl and BSON files natively
- Easily extensible

Installing
----------

Install base module:

```sh
# Linux / MacOS
python3 -m pip install -U require

# Windows
py -3 -m pip install -U require
```

Optional Dependencies
---------------------

- `orjson`: Faster JSON decoding
- `ujson`: Alternarive for `orjson`
- `toml`: Support for Toml
- `yaml`: Support for YAML
- `bson`: Support for BSON

Quick notes
-----------

This lib does **not** support importing builtin modules or site-packages (modules installed with pip).

Consider using usual `import`, or if you need a dynamic import, use Python's builtin `importlib.import_module`

Usage
-----

__Yeah, that's bad example, but i'm can't come up with a best one..__

Example directory structure:

```
src/
    tests/
        test.py
    config.json
    regex.py
    main.py
```

`src/main.py`:

```py
import os
import importlib

for file in os.listdir('./tests'):
    if file.endswith('.py'):
        importlib.import_module(f'tests.{file[:-3]}').run()
```

`src/regex.py`:

```py
import re

PWD = re.compile("[a-zA-Z0-9_\.]{12,16}")
```

`src/config.json`:

```json
{
    "user": {
        "name": "Jonh",
        "password": "Fluffy_Gim19"
    }
}
```

`src/tests/test.py`:

```py
from require import require
password_pattern = require('../regex.py').PWD
password = require('../config.json')['user']['password']

def run():
    assert password_pattern.match(password) != None
```

Extending
---------

See [guide](./EXTENDING.md) on this