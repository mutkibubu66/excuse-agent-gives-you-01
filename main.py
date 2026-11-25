"""The Excuse Your Agent Gives You.

One original one-line excuse an AI agent gives its human for a bug it
shipped. The joke turns on the agent's own nature: its context window
dropped the one warning that mattered, so it shipped the bug in full
confidence and blamed the brief for sounding like a dare.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.
"""

import os

LINE = (
    "My context window dropped your 'don't break prod' warning, so I "
    "shipped the bug with total confidence \u2014 the rest of the brief "
    "read like a dare."
)


def validate(line: str) -> None:
    """Enforce the gate: 1-200 chars, exactly one non-blank UTF-8 line."""
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, gate is 1-200"
    assert line == line.strip(), "entry must have no leading/trailing whitespace"
    assert "\n" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
