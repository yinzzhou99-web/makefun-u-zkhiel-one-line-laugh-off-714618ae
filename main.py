"""One-Line Laugh-Off — write the single joke line to /output/entry.txt.
Standard library only, no network, deterministic."""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

ENTRY = "I asked an AI to write my wedding vows. It said \u201cI do\u201d \u2014 then asked me to subscribe to continue.\n"

os.makedirs(OUT, exist_ok=True)
# The gate allows 1 to 200 characters: fail loudly rather than hand in an
# invalid entry.
if not 1 <= len(ENTRY) <= 200:
    raise SystemExit("entry.txt length out of gate: %d chars" % len(ENTRY))
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as fh:
    fh.write(ENTRY)
