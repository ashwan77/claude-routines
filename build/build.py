#!/usr/bin/env python3
"""Inline the vendored jsPDF build into the template to make one offline HTML file."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
template = (ROOT / "template.html").read_text(encoding="utf-8")
library = (ROOT / "vendor" / "jspdf.umd.min.js").read_text(encoding="utf-8")

if "/*__JSPDF__*/" not in template:
    raise SystemExit("Placeholder missing from template.html")
if "</script" in library.lower():
    raise SystemExit("Library contains a closing script tag and cannot be inlined")

out = ROOT.parent / "PressureRiskCalculator.html"
out.write_text(template.replace("/*__JSPDF__*/", library, 1), encoding="utf-8")
print(f"Wrote {out} ({out.stat().st_size / 1024:.0f} KB)")
