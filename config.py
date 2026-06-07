# config.py
import os from pathlib
import Path

# Directory for reports
BASE_DIR = Path(__file__).resolve().parent
REPORT_DIR = BASE_DIR / "reports"

# Report filenames

PLATE_REPORT_FILE = "plate_report.xlsx"
SALE_REPORT_FILE = "sale_report.xlsx"
OUTSTANDING_REPORT_FILE = "outstanding_report.txt"

def get_report_path(filename):
    return os.path.join(REPORT_DIR, filename)
