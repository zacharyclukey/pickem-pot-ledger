#!/usr/bin/env python3
"""Build the Pick'em Pot Ledger site from src.html.

Outputs:
  index.html     - standalone page for GitHub Pages (PWA head, SW registration)
  artifact.html  - fragment for publishing as a Claude artifact
"""
import pathlib, re

here = pathlib.Path(__file__).parent
src = (here / "src.html").read_text()

marker = "</style>\n"
i = src.index(marker) + len(marker)
head_part, body_part = src[:i], src[i:]

PWA_HEAD = """<meta name="theme-color" content="#EAEDE8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0E1512" media="(prefers-color-scheme: dark)">
<meta name="description" content="Weekly ledger for a pick'em pool: dues, prepay credit, kickoff lock, and who still owes.">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Pot Ledger">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon-180.png">
"""

BOOT = """<script id="boot">
if ("serviceWorker" in navigator) {
  window.addEventListener("load", function () {
    navigator.serviceWorker.register("sw.js").catch(function () {});
  });
}
</script>
"""

index = (
    "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
    + head_part
    + PWA_HEAD
    + "</head>\n<body>\n"
    + body_part.rstrip()
    + "\n"
    + BOOT
    + "</body>\n</html>\n"
)
(here / "index.html").write_text(index)
(here / "artifact.html").write_text(src)

print("index.html", len(index), "bytes")
print("artifact.html", len(src), "bytes")
