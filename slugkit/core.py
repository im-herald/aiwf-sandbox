"""Slug generation."""
import re

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(text):
    """Return a URL slug for ``text``.

    Raises TypeError when ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    lowered = text.lower()
    return _NON_ALNUM.sub("-", lowered).strip("-")


def is_slug(text):
    """Return True when ``text`` is already a slug."""
    return isinstance(text, str) and slugify(text) == text
