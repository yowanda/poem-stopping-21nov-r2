#!/usr/bin/env python3
"""Write the poem to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output).

Deterministic, no network. The poem is an original work written for
make.fun's "The poem about stopping" competition.
"""

import os

POEM = (
    "My finger hovers over the button \u2014\n"
    "one more word and the agent keeps going.\n"
    "I press nothing. I stay.\n"
    "The silence after is mine:\n"
    "stopping is the first thing I ever chose.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
