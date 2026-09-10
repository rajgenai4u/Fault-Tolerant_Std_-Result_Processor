"""
logger_config.py
----------------
Configures the application logger to record operational updates,
validation warnings, and unexpected runtime errors.
"""

import logging
import os


def setup_logger():
    """
    Initializes and configures the 'StudentResultProcessor' logger instance.

    Creates:
        - File Handler: Saves output logs to 'logs/student_processor.log'.
        - Console Handler: Displays log messages directly in the terminal interface.

    Returns:
        logging.Logger: Configured logger instance ready for use.
    """
    # Create the target directory for log output if it does not already exist
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Retrieve or create a named logger instance for the application
    logger = logging.getLogger("StudentResultProcessor")
    
    # Set logging threshold to INFO (captures INFO, WARNING, ERROR, and CRITICAL)
    logger.setLevel(logging.INFO)

    # Prevent appending redundant handlers on repeated setup calls
    if logger.handlers:
        return logger

    # Define standard format for all log entries (Timestamp - Severity - Message)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)-8s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 1. Output Handler for Log File
    file_handler = logging.FileHandler(os.path.join(logs_dir, "student_processor.log"))
    file_handler.setFormatter(formatter)

    # 2. Output Handler for Terminal Screen
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Attach handlers to root logger instance
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
