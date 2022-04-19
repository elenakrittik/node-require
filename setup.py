from setuptools import setup

setup(
    name = "node_require",
    author = "weerdy15",
    url = "https://github.com/weerdy15/node-require",
    project_urls = {
        "Issue tracker": "https://github.com/weerdy15/node-require/issues"
    },
    version = "2.0.0",
    packages = [
        "node_require"
    ],
    license = "MIT",
    description = "Like Node.js's require(), but with more supported formats",
    long_description = open('README.md', 'r').read(),
    long_description_content_type = "text/markdown",
    install_requires = [],
    extras_require = {
        "toml": [ "toml" ],
        "yaml": [ "yaml" ],
        "bson": [ "bson" ],
        "all_langs": [ "toml", "yaml", "bson" ],
    },
    python_requires = ">=3.9.7",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
        "Typing :: Typed",
    ]
)