"""Unit tests for JSON-Lens."""

import unittest
from json_lens.flattener import flatten_json, compute_json_diff


class TestJsonLens(unittest.TestCase):

    def test_flatten_nested_dict(self):
        data = {"user": {"profile": {"name": "Erik", "age": 22}}}
        flat = flatten_json(data)
        self.assertEqual(flat["user.profile.name"], "Erik")
        self.assertEqual(flat["user.profile.age"], 22)

    def test_compute_diff(self):
        d1 = {"a": 1, "b": 2}
        d2 = {"a": 1, "b": 3, "c": 4}
        diff = compute_json_diff(d1, d2)
        self.assertTrue(diff["has_changes"])
        self.assertIn("c", diff["added"])
        self.assertIn("b", diff["modified"])


if __name__ == "__main__":
    unittest.main()
