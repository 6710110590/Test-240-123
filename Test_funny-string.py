import unittest
from funnyString import Funny_string

class TestFunnyString(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Funny_string("acxz"), "Funny")

    def test_case_2(self):
        self.assertEqual(Funny_string("abc"), "Funny")

    def test_case_3(self):
        self.assertEqual(Funny_string("a"), "Funny")

    def test_case_4(self):
        self.assertEqual(Funny_string("aa"), "Funny")

    def test_case_5(self):
        self.assertEqual(Funny_string("ab"), "Funny")

    def test_case_6(self):
        self.assertEqual(Funny_string("abcd"), "Funny")

    def test_case_7(self):
        self.assertEqual(Funny_string("abba"), "Funny")

    def test_case_8(self):
        self.assertEqual(Funny_string("bcxz"), "Not Funny")

    def test_case_9(self):
        self.assertEqual(Funny_string("abd"), "Not Funny")

    def test_case_10(self):
        self.assertEqual(Funny_string("hello"), "Not Funny")

    def test_case_11(self):
        self.assertEqual(Funny_string("abcf"), "Not Funny")

if __name__ == '__main__':
    unittest.main()