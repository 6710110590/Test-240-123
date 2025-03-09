import unittest
from alternatingCharacters import alternating_characters

class TestAlternatingCharacters(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(alternating_characters(""), 0)
    
    def test_case_2(self):
        self.assertEqual(alternating_characters("C"), 0)
    
    def test_case_3(self):
        self.assertEqual(alternating_characters("CC"), 1)
    
    def test_case_4(self):
        self.assertEqual(alternating_characters("CP"), 0)
    
    def test_case_5(self):
        self.assertEqual(alternating_characters("XXXXX"), 4)
    
    def test_case_6(self):
        self.assertEqual(alternating_characters("XXXYYY"), 4)
    
    def test_case_7(self):
        self.assertEqual(alternating_characters("XXYXXY"), 2)
    
    def test_case_8(self):
        self.assertEqual(alternating_characters("ABABABAB"), 0)
    
    def test_case_9(self):
        s = "XY" * 500
        self.assertEqual(alternating_characters(s), 0)
    
    def test_case_10(self):
        s = "XXYYYXXYYYXXX"
        self.assertEqual(alternating_characters(s), 8)

if __name__ == '__main__':
    unittest.main()