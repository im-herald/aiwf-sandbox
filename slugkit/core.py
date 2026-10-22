"""Slug generation."""
import re

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(text):
    """Return a URL slug for ``text`` (lower-case ASCII letters, digits and ``-``).

    Raises TypeError when ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    lowered = text.lower()
    return _NON_ALNUM.sub("-", lowered).strip("-")
