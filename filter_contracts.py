import os
import glob

# Path to the whitelist file
whitelist_file = "cobra_testset.txt"

# Base folder
base_dir = "contracts_source_code_output"
splits = ["train", "test", "validation"]

# Read allowed contract names from txt file
with open(whitelist_file, "r") as f:
    allowed = set(line.strip().lower() for line in f if line.strip())

# Process each folder
for split in splits:
    folder = os.path.join(base_dir, split)
    sol_files = glob.glob(os.path.join(folder, "*.sol"))

    for file_path in sol_files:
        filename = os.path.basename(file_path)
        contract_name = os.path.splitext(filename)[0].lower()

        if contract_name not in allowed:
            print(f"Deleting: {file_path}")
            os.remove(file_path)
