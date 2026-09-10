"""
__init__.py
-----------
Exposes key module functions and exception definitions directly at package level.
"""

# Import specific functions and custom exceptions from sub-modules within the same package
# to expose them directly when someone imports the main package.

# The . dot notation specifies relative imports from sibling files inside the 
#results_processor directory.
#Importing validate_student_record, compute_results, setup_logger, InvalidMarksError, 
#and MissingStudentInfoError here means users can import them cleanly 
#(e.g., from results_processor import compute_results) without needing to know the 
#exact internal folder structure.

from .student_operations import validate_student_record
from .calculator import compute_results
from .logger_config import setup_logger
from .exceptions import InvalidMarksError, MissingStudentInfoError

# Define standard exported functions and classes for wildcard imports (e.g., `from package import *`).
# This controls exactly what gets exported and prevents internal helper items from leaking out.

#__all__ is a special Python list containing string names of public objects.
#It defines the explicit public API of your package. If another script executes from 
#results_processor import *, Python will only import the items listed in __all__.

__all__ = [
    "validate_student_record",
    "compute_results",
    "setup_logger",
    "InvalidMarksError",
    "MissingStudentInfoError"
]
