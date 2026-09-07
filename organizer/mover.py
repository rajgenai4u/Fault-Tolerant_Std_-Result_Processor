"""
mover.py
--------
Handles file moving, destination folder creation, and error scenarios like
duplicate files and permission issues.
"""

import os
import shutil
from .exceptions import DuplicateFileError


def move_file(source_path, destination_folder, logger):
    """
    Moves a file from source_path into destination_folder.
    Creates the destination folder if it doesn't exist.
    Handles duplicate files and permission errors.
    """
    filename = os.path.basename(source_path)

    # 1. Check if source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: '{source_path}'")

    # 2. Check/Create destination folder
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        logger.info(f"Created missing destination folder: '{destination_folder}'")

    destination_path = os.path.join(destination_folder, filename)

    # 3. Check for duplicate filenames
    if os.path.exists(destination_path):
        raise DuplicateFileError(f"File '{filename}' already exists in '{destination_folder}'.")

    # 4. Perform the file move operation
    shutil.move(source_path, destination_path)
    logger.info(f"Successfully moved: '{filename}' -> '{destination_folder}/'")