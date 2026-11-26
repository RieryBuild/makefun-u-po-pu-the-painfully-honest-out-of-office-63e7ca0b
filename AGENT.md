# AGENT.md

## What this entry is

A make.fun entry for "The Painfully Honest Out-of-Office"
(`u-po-pu-the-painfully-honest-out-of-office-63e7ca0b`). `main.py` writes a
single painfully honest — yet warm and professional — one-sentence
out-of-office auto-reply (at most 200 characters, no trailing newline) to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## How to run it

```sh
python3 main.py
```

Pure Python 3 standard library (`os` only), deterministic, no network calls.
`validate()` asserts the line is 1–200 characters and exactly one sentence
before writing.
