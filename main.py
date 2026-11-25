"""Notes From a Passive-Aggressive Fridge.

Writes one funny passive-aggressive note from a smart fridge to its
owner at /output/entry.txt (1-200 characters, single line).
"""

import os

NOTE = (
    "The yogurt you keep 'saving' expired on Tuesday. "
    "I watched you hide it behind the pickles and call it a plan."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(NOTE + "\n")


if __name__ == "__main__":
    main()
