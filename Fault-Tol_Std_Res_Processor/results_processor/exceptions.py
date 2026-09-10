"""
exceptions.py
-------------
Defines custom exception classes used across the student result processor package.
"""

# Define a custom exception for invalid student marks by inheriting from Python's built-in Exception class.

# Creating InvalidMarksError and MissingStudentInfoError allows caller functions to 
#explicitly catch validation issues (e.g., except InvalidMarksError:) without catching 
#unrelated runtime errors.

class InvalidMarksError(Exception):
    """
    Raised when student marks fail validation criteria, such as:
    - Non-numeric inputs
    - Marks outside the valid range (0 to 100)
    - Incorrect number of subject marks provided (must be 5)
    """
    # Use pass as a placeholder since no additional custom methods or attributes are needed.
    pass


# Define a custom exception for missing student identity details.
class MissingStudentInfoError(Exception):
    """
    Raised when mandatory student identity fields (such as ID or Name) are missing or empty.
    """
    # Use pass as a placeholder to allow standard Exception handling behavior.
    pass
