import sb.smartbugs
import sb.settings
import os
from datetime import datetime

LOG_FILE = "analysis_failures.log"

def log_error(message):
    """Append error messages to a log file with timestamp."""
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.write(f"{timestamp} {message}\n")

if __name__ == "__main__":
    settings = sb.settings.Settings()
    settings.update({
        "tools": [
            "confuzzius",
            "conkas",
            "manticore",
            "osiris",
            "mythril",
            "oyente",
            "sfuzz",
            "slither",
            "smartcheck"
        ],
        "files": ["contracts_source_code_output/**/*.sol"],
        "json": True,
        "overwrite": True,
        "results": "results/$TOOL/$FILENAME"
        # "quiet": True
    })

    try:
        sb.smartbugs.main(settings)
    except Exception as e:
        error_message = f"[ERROR] Analysis failed: {e}"
        print(error_message)
        log_error(error_message)
