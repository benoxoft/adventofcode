import unittest
import day14

class TestDay14(unittest.TestCase):
    
    def test_calculate_distance(self):
        self.assertEqual(1120, day14.calc_distance(14, 10, 127, 1000))
        self.assertEqual(1056, day14.calc_distance(16, 11, 162, 1000))