"""
logger_config.py
----------------
Configures logging to record both successful and failed file operations.
"""

import logging
import os


def setup_logger():
    """Sets up a logger that records activity to both a log file and console."""
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    logger = logging.getLogger("FileOrganizer")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)-8s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File handler for logs/organizer.log
    file_handler = logging.FileHandler(os.path.join(logs_dir, "organizer.log"))
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger