import sb.smartbugs
import sb.settings

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
        "files": ["cobra-plus-dataset/*.sol"],  # Your dataset path
        "json": True,         # ✅ Enable result.json
        "sarif": True,        # ✅ Enable result.sarif
        "overwrite": True,    # Optional: force re-analysis if results exist
        "results": "results/$TOOL/$RUNID/$FILENAME",  # Optional custom layout
        # "quiet": True        # Uncomment to suppress terminal output
    })

    try:
        sb.smartbugs.main(settings)
    except Exception as e:
        print(f"[ERROR] Analysis failed: {e}")
