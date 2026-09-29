"""Render the PDF from the same YAML that supplies the native al-folio web CV."""

from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent.parent
subprocess.run(
    [
        sys.executable,
        "-m",
        "rendercv",
        "render",
        "_data/cv.yml",
        "--design",
        "assets/rendercv/design.yaml",
        "--locale-catalog",
        "assets/rendercv/locale.yaml",
        "--settings",
        "assets/rendercv/settings.yaml",
    ],
    cwd=root,
    check=True,
)
