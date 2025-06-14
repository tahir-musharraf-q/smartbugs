import sb.smartbugs
import sb.settings

if __name__ == "__main__":
    settings = sb.settings.Settings()
    settings.update({
        "tools": ["conkas"],
        "files": ["samples/*.sol"],
        # "quiet": True  # optional: suppress console output
    })
    
    try:
        sb.smartbugs.main(settings)
    except Exception as e:
        print(f"Something didn't work: {e}")
