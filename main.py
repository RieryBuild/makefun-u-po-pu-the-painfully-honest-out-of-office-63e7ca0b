import os

LINE = "Thank you for your email — I'm away until Friday, and I'll reply when I'm back, hopefully before the unread count stops being a number and starts feeling like a debt."


def validate(text):
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert all(ord(ch) >= 32 for ch in text), "entry must not contain control characters"
    assert text.endswith("."), "entry must end with a single period"
    assert text.count(".") == 1, "entry must be exactly one sentence"
    return True


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
