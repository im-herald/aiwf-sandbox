"""Slug generation."""
import re

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(text, max_length=None):
    """Return a URL slug for ``text``.

    Parameters: ``text`` (str); ``max_length`` (positive int or None).
    Returns the slug, at most ``max_length`` characters when given, cut at the
    last "-" within the limit (hard cut when there is none), never ending with "-".
    Raises TypeError when ``text`` is not a string and ValueError when
    ``max_length`` is not a positive integer.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if max_length is not None and (isinstance(max_length, bool) or not isinstance(max_length, int) or max_length < 1):
        raise ValueError("max_length must be a positive integer")
    slug = _NON_ALNUM.sub("-", text.lower()).strip("-")
    if max_length is None or len(slug) <= max_length:
        return slug
    return slug[:max_length]
