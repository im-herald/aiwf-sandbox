"""Command line: python -m slugkit <text>"""
import sys

from .core import slugify


def main(argv):
    if len(argv) != 1:
        sys.stderr.write("usage: python -m slugkit <text>\n")
        return 2
    sys.stdout.write(slugify(argv[0]) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
