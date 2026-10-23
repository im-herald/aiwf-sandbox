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


class SlugifyMaxLengthTests(unittest.TestCase):
    def test_cuts_at_last_hyphen_within_limit(self):
        self.assertEqual(slugify("hello big world", max_length=11), "hello-big")

    def test_hard_cuts_when_no_hyphen_within_limit(self):
        self.assertEqual(slugify("Supercalifragilistic word", max_length=5), "super")

    def test_rejects_invalid_max_length(self):
        for bad in (0, -3, "5", 2.5):
            with self.subTest(max_length=bad):
                with self.assertRaises(ValueError) as ctx:
                    slugify("hello", max_length=bad)
                self.assertEqual(str(ctx.exception), "max_length must be a positive integer")


if __name__ == "__main__":
    unittest.main()
