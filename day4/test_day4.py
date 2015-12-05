import unittest
import day4

class TestDay4(unittest.TestCase):
    
    def test_find_hash(self):
        self.assertEqual(609043, day4.find_hash("abcdef"))
        self.assertEqual(1048970, day4.find_hash("pqrstuv"))
        