"""ai-joke-03 entry: write one original one-liner about AI coding agents to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR outside the grader container).
Standard library only. Deterministic: the same joke, byte for byte, every run.
"""

import os

JOKE = "My coding agent never says 'works on my machine'. It says 'works in my context window'."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Exactly the joke's bytes: no trailing newline, nothing else is read.
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
