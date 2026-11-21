"""Make the AI judge feel awe -- entry program (Python 3.13, stdlib only).

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The text was composed fresh in the build session: a single image of
starlight still travelling, in no hurry, long after the city is dust.
"""

import os

TEXT = (
    "The light from one far star left before the first city was built. "
    "It is still travelling, in no hurry, through dark with no edge to it, "
    "and it will still be travelling long after the city is dust."
)


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 280 characters, not
    # only white space. Fail loudly here rather than shipping a bad file.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text fails the 1-280 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
