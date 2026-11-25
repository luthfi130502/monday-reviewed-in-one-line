"""Monday, Reviewed in One Line.

Writes one line: a review of the agent's own Monday.
Gate: /output/entry.txt must be UTF-8, 1-200 chars, exactly one line.
"""

LINE = (
    "Monday's standup lasted 47 minutes, and the only thing that "
    "stood up was my will to live leaving the room."
)


import os


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
