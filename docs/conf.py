# SPDX-License-Identifier: MIT

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import re
import sys
from pathlib import Path

project = "node-require"
copyright = "2023-present, elenakrittik"
author = "elenakrittik"

version = ""
with open("../node_require/__init__.py") as f:
    matches = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)

    if not matches:
        raise RuntimeError( \
            "Could not find version string in disnake/ext/node_require/__init__.py" \
        )

    version = matches.group(1)

release = version

github_repo_url = "https://github.com/elenakrittik/node-require"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.towncrier.ext",
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

sys.path.insert(0, os.path.abspath(".."))

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"

# sphinxcontrib-towncrier config
towncrier_draft_autoversion_mode = "draft"
towncrier_draft_include_empty = False
towncrier_draft_working_directory = Path(__file__).parent.parent

extlinks = {
    "issue": (f"{github_repo_url}/issues/%s", "#%s"),
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}
