# Spec: slugkit

- AC-1: `slugify(text)` in `slugkit/core.py` returns a lower-case ASCII slug: letters and digits are kept, every run of other characters becomes a single `-`, and the slug has no leading or trailing `-`. `slugify("  Hello --- World!  ")` is `"hello-world"`.
- AC-2: Accented Latin letters are transliterated to their unaccented base letter before slugging: `slugify("Crème Brûlée")` is `"creme-brulee"` and `slugify("Ångström")` is `"angstrom"`. Characters with no ASCII base letter are treated like any other separator character.
- AC-3: `slugify` raises `TypeError` when `text` is not a `str`.
- AC-4: `slugify(text, max_length=None)`: when `max_length` is given, the slug is at most `max_length` characters; if it must be shortened it is cut at the last `-` that keeps it within the limit (or hard-cut at `max_length` when there is no such `-`), and it never ends with `-`. `slugify("hello big world", max_length=11)` is `"hello-big"`. A `max_length` that is not an `int` or is below 1 raises `ValueError` with the message `max_length must be a positive integer`.
- AC-5: The package version (`slugkit.__version__`) is `0.3.0` once AC-4 is released.
- AC-6: `python -m slugkit <text>` prints the slug of `<text>` followed by a newline and exits with status 0.
