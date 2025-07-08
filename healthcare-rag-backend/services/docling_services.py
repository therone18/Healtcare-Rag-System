import fitz  # PyMuPDF
import re

def parse_with_docling(file_path: str) -> dict:
    doc = fitz.open(file_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()

    # Try multiple patterns to support synonyms
    patient_name = re.search(r"(Patient Name|Name|Patient):\s*(.+)", full_text, re.IGNORECASE)
    visit_date = re.search(r"(Visit Date|Date of Visit):\s*(\d{4}-\d{2}-\d{2})", full_text, re.IGNORECASE)
    diagnosis = re.search(r"(Diagnosis|Assessment|Condition):\s*(.+)", full_text, re.IGNORECASE)
    medications = re.findall(r"(Medications?|Drugs?|Prescriptions?):\s*(.+)", full_text, re.IGNORECASE)
    physician = re.search(r"(Physician|Doctor|Clinician|Attending):\s*(.+)", full_text, re.IGNORECASE)

    return {
        "patient_name": patient_name.group(2).strip() if patient_name else "Unknown",
        "visit_date": visit_date.group(2).strip() if visit_date else "Unknown",
        "diagnosis": diagnosis.group(2).strip() if diagnosis else "Unknown",
        "medications": [match[1].strip() for match in medications] if medications else [],
        "physician": physician.group(2).strip() if physician else "Unknown"
    }
