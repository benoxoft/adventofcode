import unittest
import day3

class TestDay3(unittest.TestCase):
    
    def test_calculate_how_many_houses(self):
        self.assertEqual(2, day3.calculate_how_many_houses(">"))
        self.assertEqual(4, day3.calculate_how_many_houses("^>v<"))
        self.assertEqual(2, day3.calculate_how_many_houses("^v^v^v^v^v"))
        
    def test_calculate_how_many_houses_with_robo_santa(self):
        self.assertEqual(3, day3.calculate_how_many_houses_with_robo_santa("^v"))
        self.assertEqual(3, day3.calculate_how_many_houses_with_robo_santa("^>v<"))
        self.assertEqual(11, day3.calculate_how_many_houses_with_robo_santa("^v^v^v^v^v"))
    