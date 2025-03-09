import unittest
from gridChallenge import grid_challenge

class TestGridChallenge(unittest.TestCase):
    def test_case_1(self):
        grid = ["abc", "def", "ghi"]
        self.assertEqual(grid_challenge(grid), "YES")
    
    def test_case_2(self):
        grid = ["bac", "def", "ghi"]
        self.assertEqual(grid_challenge(grid), "YES")
    
    def test_case_3(self):
        grid = ["abc", "ade", "efg"]
        self.assertEqual(grid_challenge(grid), "YES")
    
    def test_case_4(self):
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        self.assertEqual(grid_challenge(grid), "YES")
    
    def test_case_5(self):
        grid = ["mpxz", "abcd", "wlmf"]
        self.assertEqual(grid_challenge(grid), "NO")
    
    def test_case_6(self):
        grid = ["abc", "hjk", "mpq", "rtv"]
        self.assertEqual(grid_challenge(grid), "YES")
    
    def test_case_7(self):
        grid = ["a"]
        self.assertEqual(grid_challenge(grid), "YES")
    
    def test_case_8(self):
        grid = ["zyx", "wvu", "tsr"]
        self.assertEqual(grid_challenge(grid), "NO")
    
    def test_case_9(self):
        grid = ["abcd", "efgh", "ijkl", "mnop"]
        self.assertEqual(grid_challenge(grid), "YES")
    
    def test_case_10(self):
        grid = ["abcd", "abce", "abcf", "abcg"]
        self.assertEqual(grid_challenge(grid), "YES")

if __name__ == '__main__':
    unittest.main()