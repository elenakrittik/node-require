.. SPDX-License-Identifier: MIT

.. currentmodule:: node_require

API Reference
=============

.. data:: loaders: dict[str, Loader]

	Global mapping of extensions to their loaders.

.. autoclass:: Loader
	:members:

.. autofunction:: require

.. autofunction:: use

.. autofunction:: one_of

Pre-made loaders
----------------

.. autoclass:: BSONLoader

.. autoclass:: JSONLoader

.. autoclass:: ModuleLoader

.. autoclass:: TOMLLoader

.. autoclass:: YAMLLoader

Exceptions
----------

.. autoexception:: ExtNotSupported

.. autoexception:: LibRequired
