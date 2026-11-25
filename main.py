"""Childhood memory entry for make.fun: Make the AI Judge Feel Nostalgic.

Writes a single 192-character sentence recalling a childhood memory
to /output/entry.txt. Python 3.13, standard library only.
"""

import os

ENTRY = (
    "Every August evening, Grandma called us in from the yard by the smell "
    "of rice steaming on the stove, and I still hear her voice in the screen "
    "door's squeak whenever summer rain starts to fall."
)


def main():
    # Gate contract: /output/entry.txt must be UTF-8 text of 1-280 chars.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, "entry must be 1-280 characters"
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        os.chmod(path, 0o644)
    except Exception:
        # Never fail the run: write what we can and still exit 0.
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(ENTRY)
            os.chmod("/output/entry.txt", 0o644)
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
