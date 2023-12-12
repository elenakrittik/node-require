# SPDX-License-Identifier: LGPL-3.0-only

__all__ = ("ExtNotSupported", "LibRequired")


class ExtNotSupported(Exception):
    """Exception that is raised when you trying to load unsupported file extension."""


class LibRequired(Exception):
    """An attempt was made to load extension some of whose dependencies were not resolved."""
