import unittest

from slugkit import slugify


class MaxLengthTests(unittest.TestCase):
    def test_spec_example(self):
        self.assertEqual(slugify("hello big world", max_length=11), "hello-big")

    def test_no_limit_needed(self):
        self.assertEqual(slugify("hello world", max_length=50), "hello-world")

    def test_hard_cut_without_separator(self):
        self.assertEqual(slugify("abcdefgh", max_length=3), "abc")

    def test_never_ends_with_dash(self):
        self.assertFalse(slugify("ab cd ef", max_length=3).endswith("-"))

    def test_invalid_max_length(self):
        for bad in (0, -1, "3", 2.5, True):
            with self.assertRaises(ValueError) as ctx:
                slugify("hello", max_length=bad)
            self.assertEqual(str(ctx.exception), "max_length must be a positive integer")


if __name__ == "__main__":
    unittest.main()
