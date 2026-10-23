import unittest

import slugkit


class VersionTests(unittest.TestCase):
    def test_version_is_0_3_0(self):
        self.assertEqual(slugkit.__version__, "0.3.0")


if __name__ == "__main__":
    unittest.main()
