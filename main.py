"""ai-joke-03 entry: one joke, written deterministically.

The program writes a single one-liner about AI coding agents to
<output_dir>/entry.txt, where <output_dir> is the MAKEFUN_OUTPUT_DIR
environment variable when set and /output otherwise. It takes no input,
uses no randomness and no network, and writes exactly the same bytes on
every run: the machine has no excuse for a different punchline.
"""

import os

JOKE = "'It works on my machine,' said my AI coding agent, who is the machine."

DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"


def entry_path() -> str:
    """Resolve where the entry file belongs for this run."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return os.path.join(output_dir, ENTRY_FILENAME)


def main() -> None:
    # The contract: UTF-8 text, 1-280 characters, never whitespace-only.
    # Fail loudly rather than write an entry the scorer would refuse.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise ValueError("joke violates the entry contract")
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
