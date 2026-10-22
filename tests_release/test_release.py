"""Release consistency (CI tier only): the package version must have a CHANGELOG entry."""
import pathlib
import re
import unittest

import slugkit

ROOT = pathlib.Path(__file__).resolve().parent.parent


class ReleaseConsistencyTests(unittest.TestCase):
    def test_changelog_has_entry_for_current_version(self):
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        headings = re.findall(r"^## (\S+)", changelog, flags=re.MULTILINE)
        self.assertIn(
            slugkit.__version__,
            headings,
            f"CHANGELOG.md has no '## {slugkit.__version__}' entry for the package version",
        )


if __name__ == "__main__":
    unittest.main()
