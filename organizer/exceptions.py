"""
exceptions.py
-------------
Defines custom exception classes for file organizing operations.
"""

class UnsupportedFileError(Exception):
    """Raised when encountering a file type/extension that is not mapped to any category."""
    pass


class DuplicateFileError(Exception):
    """Raised when a file with the same name already exists in the destination folder."""
    pass