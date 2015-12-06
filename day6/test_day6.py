import unittest
import day6

class TestDay6(unittest.TestCase):
    
    def old_test_execute_command(self):
        day6.execute_command("turn on 0,0 through 999,999")
        self.assertEqual(1000000, len(day6.lights))
        
        day6.lights = {}
        day6.execute_command("toggle 0,0 through 999,0")
        self.assertEqual(1000, len(day6.lights))

        day6.lights = {}
        day6.execute_command("turn off 499,499 through 500,500")
        self.assertEqual(0, len(day6.lights))
        
    def test_execute_command(self):
        day6.execute_command("turn on 0,0 through 0,0")
        self.assertEqual(1, sum(day6.lights.values()))
        
        day6.lights = {}
        day6.execute_command("toggle 0,0 through 999,999")
        self.assertEqual(2000000, sum(day6.lights.values()))
        
        