import unittest
import day11

EXAMPLE_1 = 'hijklmmn'
EXAMPLE_2 = 'abbceffg'
EXAMPLE_3 = 'abbcegjk'

class TestDay11(unittest.TestCase):
    
    def test_day11(self):
        self.assertTrue(day11.val_rule_1(EXAMPLE_1))
        self.assertFalse(day11.val_rule_2(EXAMPLE_1))
        self.assertFalse(day11.val_rule_3(EXAMPLE_1))
        
        self.assertFalse(day11.val_rule_1(EXAMPLE_2))
        self.assertTrue(day11.val_rule_2(EXAMPLE_2))
        self.assertTrue(day11.val_rule_3(EXAMPLE_2))
        
        self.assertFalse(day11.val_rule_1(EXAMPLE_3))
        self.assertTrue(day11.val_rule_2(EXAMPLE_3))
        self.assertFalse(day11.val_rule_3(EXAMPLE_3))
        
    def test_increment_letter(self):
        self.assertEqual('abcdffaa', day11.increment_password(list('abcdefgh')))
        self.assertEqual('ghjaabcc', day11.increment_password(list('ghijklmn')))