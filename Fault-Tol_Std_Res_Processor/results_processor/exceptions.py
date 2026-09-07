"""
exceptions.py
-------------
Defines custom exception classes used across the student result processor package.
"""

class InvalidMarksError(Exception):
    """
    Raised when student marks fail validation criteria, such as:
    - Non-numeric inputs
    - Marks outside the valid range (0 to 100)
    - Incorrect number of subject marks provided (must be 5)
    """
    pass


class MissingStudentInfoError(Exception):
    """
    Raised when mandatory student identity fields (such as ID or Name) are missing or empty.
    """
    pass