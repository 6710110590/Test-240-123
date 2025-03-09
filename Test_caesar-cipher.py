import unittest
from caesarCipher import caesar_cipher

class TestJuliusCaesar(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(caesar_cipher("abc", 1), "bcd")
    
    def test_case_2(self):
        self.assertEqual(caesar_cipher("ABC", 1), "BCD")
    
    def test_case_3(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc")
    
    def test_case_4(self):
        self.assertEqual(caesar_cipher("XYZ", 3), "ABC")
    
    def test_case_5(self):
        self.assertEqual(caesar_cipher("abc123", 2), "cde123")
    
    def test_case_6(self):
        self.assertEqual(caesar_cipher("Hello, World!", 5), "Mjqqt, Btwqi!")
    
    def test_case_7(self):
        self.assertEqual(caesar_cipher("", 10), "")
    
    def test_case_8(self):
        self.assertEqual(caesar_cipher("abc", 26), "abc")
    
    def test_case_9(self):
        self.assertEqual(caesar_cipher("abc", 52), "abc")
    
    def test_case_10(self):
        self.assertEqual(caesar_cipher("abc", 0), "abc")

if __name__ == '__main__':
    unittest.main()