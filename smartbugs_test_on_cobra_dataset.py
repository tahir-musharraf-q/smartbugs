import sb.smartbugs
import sb.settings
import os
from datetime import datetime

LOG_FILE = "analysis_failures.log"

def filter_files_with_pragma(file_list):
    valid_files = []
    for path in file_list:
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read(200)  # Only check top of file
                if "pragma solidity" in content:
                    valid_files.append(path)
        except Exception as e:
            print(f"Skipped {path}: {e}")
    return valid_files

# Filter .sol files in your target folders
import glob
all_files = glob.glob("contracts_source_code_output/**/*.sol", recursive=True)
filtered_files = filter_files_with_pragma(all_files)


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
        "files": filtered_files,
        "json": True,
        # "overwrite": False, # start fresh each time
        "results": "results/$TOOL/$FILENAME",
        # "quiet": True,
        "timeout": 300 # 5 minutes timeout for each file
    })

    try:
        sb.smartbugs.main(settings)
    except Exception as e:
        error_message = f"[ERROR] Analysis failed: {e}"
        print(error_message)
        log_error(error_message)
