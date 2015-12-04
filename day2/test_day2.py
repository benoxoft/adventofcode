import unittest
import day2

class TestDay2(unittest.TestCase):
    
    def test_calculate_paper(self):
        self.assertEqual(58, day2.calculate_paper(2,3,4))
        self.assertEqual(43, day2.calculate_paper(1,1,10))
        
    def test_calculate_ribbon(self):
        self.assertEqual(34, day2.calculate_ribbon(2, 3, 4))
        self.assertEqual(14, day2.calculate_ribbon(1, 1, 10))