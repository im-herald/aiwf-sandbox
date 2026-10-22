import unittest

from slugkit import slugify


class SlugifyTests(unittest.TestCase):
    def test_lowercases_and_joins_words(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_collapses_runs_of_separators(self):
        self.assertEqual(slugify("  Hello --- World!  "), "hello-world")

    def test_keeps_digits(self):
        self.assertEqual(slugify("Release 2 Notes"), "release-2-notes")

    def test_rejects_non_strings(self):
        with self.assertRaises(TypeError):
            slugify(42)


if __name__ == "__main__":
    unittest.main()
