"""Integration checks for the built site, including links and native feature output."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parent.parent / "_site"
ORIGIN = "julio-am.github.io"
errors = []


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.text = []
        self.classes = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.classes.update(attrs.get("class", "").split())
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])

    def handle_data(self, data):
        self.text.append(data)


required = {
    "index.html": ["<h1"],
    "cv/index.html": ["<h1"],
    "publications/index.html": ["<h1"],
    "projects/index.html": ["<h1"],
    "blog/index.html": ["<h1"],
    "404.html": ["<h1"],
    "feed.xml": ["<feed"],
    "sitemap.xml": ["<urlset"],
}

for filename, markers in required.items():
    path = ROOT / filename
    if not path.exists():
        errors.append(f"Missing output: {filename}")
        continue
    content = path.read_text()
    for marker in markers:
        if marker not in content:
            errors.append(f"{filename}: missing expected feature output {marker!r}")

pdf = ROOT / "assets/pdf/cv.pdf"
if not pdf.exists() or not pdf.read_bytes().startswith(b"%PDF-"):
    errors.append("Downloadable CV is missing or is not a PDF")

pages = list(ROOT.rglob("*.html"))
expected_classes = {
    "index.html": "personal-home",
    "cv/index.html": "cv",
    "publications/index.html": "publications",
    "projects/index.html": "project-list",
    "blog/index.html": "personal-post-list",
}
for path in pages:
    page = Page()
    content = path.read_text()
    page.feed(content)
    expected = expected_classes.get(path.relative_to(ROOT).as_posix())
    if expected and expected not in page.classes:
        errors.append(f"{path.relative_to(ROOT)}: missing native feature container {expected}")
    for failure in ("Liquid Exception", "CV rendering is unavailable", "No CV data found"):
        if failure in content:
            errors.append(f"{path.relative_to(ROOT)}: {failure}")
    for link in page.links:
        parts = urlsplit(link)
        if parts.scheme not in ("", "http", "https") or parts.netloc not in ("", ORIGIN):
            continue
        if not parts.path:
            continue
        target = (ROOT / unquote(parts.path).lstrip("/")) if parts.path.startswith("/") else (path.parent / unquote(parts.path))
        if target.is_dir():
            target /= "index.html"
        if not target.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken local link {link}")

if errors:
    print("\n".join(sorted(set(errors))))
    sys.exit(1)

print(f"Verified {len(pages)} HTML pages, native CV/publications/blog output, PDF, feeds, and local links.")
