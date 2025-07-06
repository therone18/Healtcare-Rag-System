def parse_with_docling(file_path: str) -> dict:
    """
    Simulated IBM DocLing parser output.
    In the real implementation, this function would call IBM DocLing's API
    and return structured JSON from the PDF.

    For now, it returns a mocked dictionary.
    """
    return {
        "patient_name": "Jane Doe",
        "visit_date": "2025-06-15",
        "diagnosis": "Hypertension",
        "medications": ["Lisinopril"],
        "physician": "Dr. Smith"
    }
