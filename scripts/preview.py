"""Serve the Jekyll build for visual previews; run the build first."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--host", default="0.0.0.0")
parser.add_argument("--port", type=int, default=4173)
parser.add_argument("--strictPort", action="store_true", help="The server always uses the exact requested port.")
args = parser.parse_args()
site = Path(__file__).resolve().parent.parent / "_site"
if not (site / "index.html").exists():
    raise SystemExit("Build the site first: bundle exec jekyll build")
handler = partial(SimpleHTTPRequestHandler, directory=str(site))
ThreadingHTTPServer((args.host, args.port), handler).serve_forever()
