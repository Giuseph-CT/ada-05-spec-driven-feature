from pathlib import Path
import sys

required_files = [
    "AGENTS.md",
    "README.md",
    "REQUIREMENTS.md",
    "SPEC.md",
    "ARCHITECTURE.md",
    "TASKS.md",
    "docs/REPO_MAP.md",
    "GEMINI.md",
    "scripts/verify_repo.sh"
]

missing = [path for path in required_files if not Path(path).exists()]

if missing:
    print("REPO_CONTRACT: FAIL")
    for path in missing:
        print(f"Missing essential file: {path}")
    sys.exit(1)

print("REPO_CONTRACT: PASS")
sys.exit(0)