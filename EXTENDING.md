Example plugin that loads `.hjson` files using [`hjson`](https://pypi.org/project/hjson) library:

```python
import os
import typing as T

from node_require import (
    one_of, # Import one of given modules
    Loader, # ABC for all plugins
)

class HJSONLoader(Loader):
    """
    A plugin loader to load HJSON files
    """
    def __init__(self) -> None:
        self.hjson = one_of(['hjson']) # Assign the hjson module to variable
        self.extensions: T.List[str] = ['.hjson'] List of extensions that plugin can load
        self.deps: T.List[str] = ['hjson'] # List of libraries required to load files of approritate extension(-s)
        self.optional_deps: T.Dict[str, str] = {} # A dictionary of libraries that are not required but can, e.g.,
                                                  # speed up decoding (or anything else) of files. It is a mapping
                                                  # of library name to description for what it is needed.
    
    def load(self, path: str, file: str) -> T.Dict[str, T.Any]: # A function that is called by the library when
                                                                # user trying to require() .hjson file
        try:
            with open(os.path.abspath(path) + '/' + file, 'r') as fp:
                return dict(self.hjson.loads(fp.read())) # `hjson.loads()` returning `collections.OrderedDict`,
                                                         # but want to it be a regular dictionary. That's why we
                                                         # manually converting it to `dict`
        except FileNotFoundError:
            raise ValueError(f"No such file: {file}") from None

loader = HJSONLoader
```

Then, assuming that the code above you put into `my_hjson_plugin.py` file, you can `use()` it from anywhere:

```python
# "Traditional" method, can be used in the same directory or one directory below the file
from my_hjson_plugin import loader
# Using `require()`, can be in any place on the disk
import node_require as node
loader = node.require("./my_hjson_loader.py")

# Then call `use()` to register plugin
node.use(loader)

# Now, you can `require()` `.hjson` files from anywhere of your code, even
# in other files (i.e., there is no need to `use()` the loader in each file)
data = node.require("my_awesome_hjson_file.hjson")
print(data) # Wow, dictionary!
```

You can event put the loader in your library, upload to [PyPI](https://pypi.org/) and distribute as a Python package!
