import unittest
from twoCharacters import alternate_two_characters

class TestTwoCharactor(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(alternate_two_characters("beabeefeab"), 5)
    
    def test_case_2(self):
        self.assertEqual(alternate_two_characters("a"), 0)
    
    def test_case_3(self):
        self.assertEqual(alternate_two_characters("ab"), 2)
    
    def test_case_4(self):
        self.assertEqual(alternate_two_characters("aaaa"), 0)
    
    def test_case_5(self):
        self.assertEqual(alternate_two_characters("abababab"), 8)
    
    def test_case_6(self):
        self.assertEqual(alternate_two_characters("abcabcabc"), 6)
    
    def test_case_7(self):
        self.assertEqual(alternate_two_characters("abcde"), 2)
    
    def test_case_8(self):
        self.assertEqual(alternate_two_characters("asvkugfiugsaldd"), 4)
    
    def test_case_9(self):
        self.assertEqual(alternate_two_characters("asdcbsdcagfsdbgdfanfghbsfdab"), 8)
    
    def test_case_10(self):
        self.assertEqual(alternate_two_characters("asvkugfiugsalddlasguifgukvsa"), 0)

if __name__ == '__main__':
    unittest.main()