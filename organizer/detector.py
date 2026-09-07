"""
detector.py
-----------
Identifies target categories for files based on their extensions.
"""

import os
from .exceptions import UnsupportedFileError

# Mapping file extensions to target folder names
EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Text": [".txt", ".md", ".rtf"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".pptx"],
    "Data": [".csv", ".json", ".xml", ".sql"],
    "Archives": [".zip", ".tar", ".gz", ".7z"]
}


def detect_category(file_path):
    """
    Determines the category folder based on file extension.
    
    Raises:
        UnsupportedFileError: If the extension is not configured in EXTENSION_MAP.
    """
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if not ext:
        raise UnsupportedFileError(f"File '{os.path.basename(file_path)}' has no file extension.")

    for category, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return category

    raise UnsupportedFileError(f"Extension '{ext}' for file '{os.path.basename(file_path)}' is unsupported.")