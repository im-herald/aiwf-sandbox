"""Slug generation."""
import re

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(text, max_length=None):
    """Return a URL slug for ``text``.

    ``max_length``, when given, caps the slug length: the slug is cut at the
    last ``-`` that keeps it within the limit, or hard-cut at ``max_length``
    when there is no such ``-``.

    Raises TypeError when ``text`` is not a string, and ValueError when
    ``max_length`` is not a positive integer.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if max_length is not None and (not isinstance(max_length, int) or max_length < 1):
        raise ValueError("max_length must be a positive integer")
    lowered = text.lower()
    slug = _NON_ALNUM.sub("-", lowered).strip("-")
    if max_length is not None and len(slug) > max_length:
        cut = slug.rfind("-", 0, max_length + 1)
        slug = slug[:cut] if cut > 0 else slug[:max_length]
    return slug
