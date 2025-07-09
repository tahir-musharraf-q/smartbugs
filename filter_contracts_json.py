import os
import glob
import json
from tqdm import tqdm

# Path to the whitelist JSON file
whitelist_file = "test_contracts.json"

# Base folder
base_dir = "contracts_source_code_output"
splits = ["train", "test", "validation"]

# Read allowed contract addresses from JSON (normalized to lowercase)
with open(whitelist_file, "r") as f:
    allowed = set(addr.strip().lower() for addr in json.load(f))

# Process each split folder
for split in splits:
    folder = os.path.join(base_dir, split)
    sol_files = glob.glob(os.path.join(folder, "*.sol"))
    total = len(sol_files)
    if total == 0:
        continue

    print(f"\nProcessing split '{split}' ({total} files):")
    for file_path in tqdm(sol_files, desc=f"{split}", unit="file"):
        contract_name = os.path.splitext(os.path.basename(file_path))[0].lower()
        if contract_name not in allowed:
            os.remove(file_path)
    print(f"→ Done with '{split}'.")
