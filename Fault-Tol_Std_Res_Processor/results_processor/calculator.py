"""
calculator.py
-------------
Computes mathematical summaries including totals, percentages, letter grades, and pass/fail statuses.
"""

def compute_results(validated_student):
    """
    Calculates total marks, overall percentage, letter grade, and pass status.

    Grade Scale:
      - Percentage >= 90: A+
      - Percentage >= 80: A
      - Percentage >= 70: B
      - Percentage >= 60: C
      - Percentage >= 50: D
      - Percentage < 50: F

    Pass Criteria:
      - Overall percentage >= 40 AND every individual subject mark is >= 40.

    Args:
        validated_student (dict): Validated student dictionary containing float marks.

    Returns:
        dict: Detailed execution performance breakdown.

    Raises:
        ZeroDivisionError: If the subject list length evaluates to 0.
    """
    marks = validated_student["marks"]
    num_subjects = len(marks)

    # Protect against unexpected zero denominator calculation issues
    if num_subjects == 0:
        raise ZeroDivisionError("Cannot calculate percentage for zero subjects.")

    total_marks = sum(marks)
    percentage = (total_marks / (num_subjects * 100)) * 100

    # Determine letter grade mapping
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Evaluate pass/fail status based on a 40-mark passing threshold per subject
    status = "PASS" if all(mark >= 40 for mark in marks) else "FAIL"

    return {
        "student_id": validated_student["student_id"],
        "name": validated_student["name"],
        "total": total_marks,
        "percentage": round(percentage, 2),
        "grade": grade,
        "status": status
    }