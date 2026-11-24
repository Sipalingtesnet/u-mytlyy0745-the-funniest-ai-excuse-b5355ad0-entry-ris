#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt (UTF-8, single line, no trailing newline)."""

import os

LINE = "I broke your task into nine subtasks and assigned all nine to me. I'm still waiting on me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
