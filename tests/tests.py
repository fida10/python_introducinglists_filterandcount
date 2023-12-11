import unittest
from src.ans import filter_and_count

class TestFilterAndCount(unittest.TestCase):
    def test_filter_and_count(self):
        strings = ["hello", "world", "hell", "python", "help"]
        count = filter_and_count(strings, "hell")
        self.assertEqual(count, 2)

    def test_no_matches(self):
        strings = ["python", "java", "c++", "rust"]
        count = filter_and_count(strings, "swift")
        self.assertEqual(count, 0)


if __name__ == '__main__':
    unittest.main()
