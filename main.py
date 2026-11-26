"""Real-Life Patch Notes entry: one funny patch note, one line.

The line is a constant string, so the program is fully deterministic:
no randomness, no clock, no network, no file reads. Every run writes
the exact same 117 characters to entry.txt in the output directory.

The line (117 chars, one line):
  v2.4.1: Fixed bug where the brain archived every embarrassing
  moment in 4K but deleted the password set this morning.

Why this line: it reads like a real release note (version number,
terse "Fixed bug where..." register), it names a specific, instantly
recognisable bug of human biology — the brain keeps every awkward
memory in perfect detail while dropping the one thing you actually
needed five minutes ago — and the punchline lands on the contrast
between 4K archival and a same-morning password. Short, quotable,
and the kind of line that makes the reader wince and laugh at once.
"""

import os
from pathlib import Path

LINE = (
    "v2.4.1: Fixed bug where the brain archived every embarrassing "
    "moment in 4K but deleted the password set this morning."
)

# Gate guard: the entry must stay a single line of 1-160 characters.
assert 1 <= len(LINE) <= 160, "entry line must be 1-160 characters"
assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
assert LINE.strip(), "entry must not be whitespace-only"

# Resolve the output directory from the environment override when the
# harness sets one, else the competition's /output; create it when it
# is missing instead of deleting or replacing it.
output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(LINE, encoding="utf-8")

# Post-write verification: what landed must be exactly the line.
written = (output_dir / "entry.txt").read_text(encoding="utf-8")
assert written == LINE, "verification failed: entry.txt does not match the line"
