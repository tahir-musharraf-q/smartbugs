import os
import json
from tqdm import tqdm

# ─── User configuration ────────────────────────────────────────────────
# Root directory containing one subfolder per tool
TOOLS_ROOT = "results"
# Directory to write per-tool reports
OUTPUT_ROOT = "smartbug_output"
# ────────────────────────────────────────────────────────────────────────

def process_tool(tool_name):
    tool_dir = os.path.join(TOOLS_ROOT, tool_name)
    report = {}
    safe_count = 0

    entries = [
        entry
        for entry in sorted(os.listdir(tool_dir))
        if os.path.isdir(os.path.join(tool_dir, entry))
    ]
    total = len(entries)

    # progress bar over contracts
    for entry in tqdm(entries, desc=f"{tool_name}", unit="contract"):
        # derive contract address (strip ".sol")
        if entry.lower().endswith(".sol"):
            contract = entry[:-4].lower()
        else:
            contract = entry.lower()

        result_file = os.path.join(tool_dir, entry, "result.json")
        vulns = set()

        if os.path.isfile(result_file):
            try:
                data = json.load(open(result_file))
                for f in data.get("findings", []):
                    name = f.get("name")
                    if name:
                        vulns.add(name)
            except json.JSONDecodeError:
                # malformed JSON: treat as safe
                pass

        if not vulns:
            report[contract] = "safe"
            safe_count += 1
        else:
            report[contract] = ",".join(sorted(vulns))

    # write report
    os.makedirs(OUTPUT_ROOT, exist_ok=True)
    out_path = os.path.join(OUTPUT_ROOT, f"{tool_name}_report.json")
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2)

    # summary
    print(f"\n🔧 Tool: {tool_name}")
    print(f"  • Contracts processed: {total}")
    print(f"  • Marked safe (empty findings): {safe_count}")
    print(f"  • Report written to: {out_path}\n")

def main():
    if not os.path.isdir(TOOLS_ROOT):
        print(f"[!] Tools root directory not found: {TOOLS_ROOT}")
        return

    tools = [
        d for d in sorted(os.listdir(TOOLS_ROOT))
        if os.path.isdir(os.path.join(TOOLS_ROOT, d))
    ]

    print(f"Found {len(tools)} tools in {TOOLS_ROOT}\n")
    for tool in tools:
        process_tool(tool)

if __name__ == "__main__":
    main()
