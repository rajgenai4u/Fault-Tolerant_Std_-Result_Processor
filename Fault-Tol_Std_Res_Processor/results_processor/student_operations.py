"""
student_operations.py
---------------------
Provides validation logic to sanitize raw student input dictionary objects.
"""

from .exceptions import InvalidMarksError, MissingStudentInfoError


def validate_student_record(student_data):
    """
    Validates a raw dictionary containing student information.

    Validation Checks:
    1. Ensures student_id and name are present and non-empty strings.
    2. Validates that 'marks' is a sequence with exactly 5 subjects.
    3. Verifies every individual mark is a numeric value within 0 and 100.

    Args:
        student_data (dict): Dictionary containing keys 'student_id', 'name', and 'marks'.

    Returns:
        dict: Sanitized student record with numerical float conversion applied to marks.

    Raises:
        MissingStudentInfoError: If student identifier or name is missing/blank.
        InvalidMarksError: If marks list length is not 5 or contains invalid values.
    """
    # Extract expected keys from the input dictionary safely using .get()
    student_id = student_data.get("student_id")
    name = student_data.get("name")
    marks = student_data.get("marks")

    # 1. Validate existence of essential student identifying information
    if not student_id or not str(student_id).strip():
        raise MissingStudentInfoError("Student record is missing a valid 'student_id'.")

    if not name or not str(name).strip():
        raise MissingStudentInfoError(f"Student ID '{student_id}' is missing a valid 'name'.")

    # 2. Validate container type and length of marks collection
    if not isinstance(marks, (list, tuple)):
        raise InvalidMarksError(f"Marks for student '{name}' must be provided as a list or tuple.")

    if len(marks) != 5:
        raise InvalidMarksError(f"Student '{name}' must have marks for exactly 5 subjects (received {len(marks)}).")

    # 3. Validate data type and numeric limits for individual subject marks
    validated_marks = []
    for idx, mark in enumerate(marks, start=1):
        # Exclude booleans explicitly since bool inherits from int in Python
        if isinstance(mark, bool) or not isinstance(mark, (int, float)):
            raise InvalidMarksError(f"Student '{name}': Subject {idx} mark '{mark}' is non-numeric.")

        if mark < 0 or mark > 100:
            raise InvalidMarksError(f"Student '{name}': Subject {idx} mark {mark} is outside the valid 0–100 range.")

        # Cast valid integer or float mark to a standard float type
        validated_marks.append(float(mark))

    # Return sanitized and formatted student record
    return {
        "student_id": str(student_id).strip(),
        "name": str(name).strip(),
        "marks": validated_marks
    }
