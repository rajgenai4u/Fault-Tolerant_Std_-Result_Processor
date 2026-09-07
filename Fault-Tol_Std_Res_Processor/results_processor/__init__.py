"""
__init__.py
-----------
Exposes key module functions and exception definitions directly at package level.
"""

from .student_operations import validate_student_record
from .calculator import compute_results
from .logger_config import setup_logger
from .exceptions import InvalidMarksError, MissingStudentInfoError

# Define standard exported functions for wildcard package imports
__all__ = [
    "validate_student_record",
    "compute_results",
    "setup_logger",
    "InvalidMarksError",
    "MissingStudentInfoError"
]