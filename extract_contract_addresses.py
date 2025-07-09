import os
import json

# Root folder containing tool subfolders
ROOT_DIR = "results"

# Output files
OUT_TXT = "unique_contracts.txt"
OUT_JSON = "unique_contracts.json"

# Set to store unique contract addresses
contract_addresses = set()

# Traverse each tool folder
for tool_name in sorted(os.listdir(ROOT_DIR)):
    tool_path = os.path.join(ROOT_DIR, tool_name)
    if not os.path.isdir(tool_path):
        continue

    for entry in os.listdir(tool_path):
        if entry.lower().endswith(".sol"):
            address = entry[:-4].lower()  # Strip .sol extension
            contract_addresses.add(address)

# Sort addresses before saving
sorted_addresses = sorted(contract_addresses)

# Save to text file (one address per line)
with open(OUT_TXT, "w") as f:
    for addr in sorted_addresses:
        f.write(addr + "\n")

# Save to JSON list
with open(OUT_JSON, "w") as f:
    json.dump(sorted_addresses, f, indent=2)

# Report
print(f"✅ Extracted {len(sorted_addresses)} unique contract addresses.")
print(f"→ Saved to: {OUT_TXT}")
print(f"→ Saved to: {OUT_JSON}")
