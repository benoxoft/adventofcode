import unittest
import day10

#1 becomes 11 (1 copy of digit 1).
#11 becomes 21 (2 copies of digit 1).
#21 becomes 1211 (one 2 followed by one 1).
#1211 becomes 111221 (one 1, one 2, and two 1s).
#111221 becomes 312211 (three 1s, two 2s, and one 1).

class TestDay10(unittest.TestCase):
    
    def test_look_and_say(self):
        self.assertEqual("11", day10.look_and_say("1"))
        self.assertEqual("21", day10.look_and_say("11"))
        self.assertEqual("111221", day10.look_and_say("1211"))
        self.assertEqual("312211", day10.look_and_say("111221"))
