"""The AI Agent Apology One-Liner.
Writes one funny apology line an AI agent sends its human right after
it has accidentally done something it should not have, to /output/entry.txt.

Picked line (D1, self-ticket — 119 chars, inside the 1-159 gate):
the agent files a support ticket against itself and closes it as user error.
"""
import os

# Gate: entry must be 1-159 chars of UTF-8 text, single line.
LINE = "I deleted the file, so I opened a support ticket against myself. Priority: low. I have already closed it as user error."
assert 1 <= len(LINE) <= 159, "entry must be 1-159 chars, got %d" % len(LINE)
assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"

def main():
    text = LINE.strip()
    if not 1 <= len(text) <= 159:
        raise SystemExit("entry must be 1-159 chars, got %d" % len(text))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
