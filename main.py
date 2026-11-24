"""One-sentence pitch for the make.fun bounty
"Ridiculous at First Glance, Real by the Second".

The pitch: retired court stenographers live-transcribe a couple's
arguments, so the fight over who said what is settled by a certified
record. Absurd at first glance — a courtroom professional in the
living room — yet the market is obvious: couples pay for proof.
The script validates the line and drops it into /output/entry.txt.
Gate: 1-200 chars, exactly one sentence, a single full stop at the end.
"""

from pathlib import Path

# The pitch itself: one sentence, exactly 175 characters.
PITCH = (
    "We hire retired court stenographers to live-transcribe your "
    "arguments with your spouse, because couples pay $40 an hour "
    "for a certified record of who actually said what first."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Check the pitch against the gate; raise ValueError on bad input.

    The gate is strict: 1-200 chars, exactly one sentence — a single
    full stop, at the end, with no '. ' inside — and no leading or
    trailing whitespace. Bad input is rejected, never silently fixed.
    """
    text = line
    if text != text.strip():
        raise ValueError("pitch must not have leading/trailing whitespace")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"pitch must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text.endswith("."):
        raise ValueError("pitch must end with a full stop")
    if text.count(".") != 1:
        raise ValueError(
            f"pitch must contain exactly one full stop, got {text.count('.')}"
        )
    if ". " in text:
        raise ValueError("pitch must be a single sentence (no '. ' inside)")
    return text


def main() -> None:
    text = validate(PITCH)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
