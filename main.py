#!/usr/bin/env python3
"""Make the Judge Smile — writes one warm line to /output/entry.txt."""
import os

LINE = (
    "At 6:10 this morning the driver held the bus doors while my "
    "82-year-old neighbour shuffled up with her market roses — then she "
    "tucked one behind his mirror, and he drove the whole route grinning."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
