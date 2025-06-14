import os
import glob

# Root directory
base_dir = "contracts_source_code_output"

# Subfolders to process
splits = ["train", "test", "validation"]

for split in splits:
    folder = os.path.join(base_dir, split)
    pattern = os.path.join(folder, "*.solc")

    for solc_file in glob.glob(pattern):
        sol_file = solc_file[:-5] + ".sol"  # Replace .solc with .sol
        os.rename(solc_file, sol_file)
        print(f"Renamed: {solc_file} -> {sol_file}")
