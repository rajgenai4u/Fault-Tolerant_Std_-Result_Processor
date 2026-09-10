"""
main.py
-------
Main execution module. Processes a dataset of student records inside a
fault-tolerant loop that catches errors, logs issues, and continues execution.
"""

# Import validated processing routines, logger utility, and custom exceptions from the results_processor package
from results_processor import (
    validate_student_record,
    compute_results,
    setup_logger,
    InvalidMarksError,
    MissingStudentInfoError
)


def process_student_batch(student_records):
    """
    Iterates through a list of raw student records, processing each individual item.
    Ensures that processing failure for one student does not stop execution for the rest.

    Args:
        student_records (list): List of dictionaries containing raw student inputs.

    Returns:
        list: Collection of processed summary result dictionaries for valid students.
    """
    # Initialize logger configuration to record process events and errors
    logger = setup_logger()
    logger.info(f"Starting batch result processing for {len(student_records)} student records.")

    # Initialize container to hold successfully processed output dicts
    successful_results = []

    # Loop through each student record individually to ensure fault tolerance
    for record in student_records:
        # Fallback identifier for reporting in log messages when names are unavailable
        student_identifier = record.get("name") or record.get("student_id") or "Unknown Student"

        try:
            # Step 1: Validate input fields and numeric marks ranges
            validated_student = validate_student_record(record)

            # Step 2: Calculate total, percentage, grade, and pass status
            result = compute_results(validated_student)
            successful_results.append(result)

            # Log successful processing details
            logger.info(
                f"Successfully processed: {result['name']} (ID: {result['student_id']}) "
                f"| Total: {result['total']}/500 | Percentage: {result['percentage']}% "
                f"| Grade: {result['grade']} | Status: {result['status']}"
            )

        # Fault-tolerant exception handling catches specific error types independently
        except MissingStudentInfoError as e:
            logger.error(f"Missing Information Error [{student_identifier}]: {e}")
            
        except InvalidMarksError as e:
            logger.error(f"Invalid Marks Error [{student_identifier}]: {e}")
            
        except ZeroDivisionError as e:
            logger.error(f"Calculation Error [{student_identifier}]: {e}")
            
        except Exception as e:
            # Catch any unexpected runtime errors without terminating batch execution
            logger.critical(f"Unexpected Critical Error [{student_identifier}]: {e}", exc_info=True)

    # Log execution summary after completing the loop
    logger.info(
        f"Batch processing complete. "
        f"Successfully processed {len(successful_results)} out of {len(student_records)} records."
    )

    return successful_results


if __name__ == "__main__":
    # Test batch demonstrating valid input, non-numeric values, out-of-range scores, and missing details
    dataset = [
        {"student_id": "S101", "name": "Alice Smith", "marks": [85, 90, 78, 92, 88]},     # Valid student
        {"student_id": "S102", "name": "Bob Jones", "marks": [45, "invalid", 60, 55, 50]}, # Non-numeric mark
        {"student_id": "S103", "name": "Charlie Brown", "marks": [70, 80, 105, 65, 75]}, # Mark > 100
        {"student_id": "", "name": "David Miller", "marks": [60, 60, 60, 60, 60]},         # Missing Student ID
        {"student_id": "S105", "name": "Eva Green", "marks": [35, 80, 75, 90, 85]},        # Fail condition check
        {"student_id": "S106", "name": "Frank Castle", "marks": [70, 80, 90]},             # Incorrect subject count
    ]

    # Execute batch processing
    results = process_student_batch(dataset)
