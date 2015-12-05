import unittest
import day5

class TestDay5(unittest.TestCase):
    
    def test_judge_word_part1(self):
        self.assertEqual(day5.NICE, day5.judge_word_part1("ugknbfddgicrmopn"))
        self.assertEqual(day5.NICE, day5.judge_word_part1("aaa"))
        self.assertEqual(day5.NAUGHTY, day5.judge_word_part1("jchzalrnumimnmhp"))
        self.assertEqual(day5.NAUGHTY, day5.judge_word_part1("haegwjzuvuyypxyu"))
        self.assertEqual(day5.NAUGHTY, day5.judge_word_part1("dvszwmarrgswjxmb"))
        
    def test_judge_word_part2(self):
        self.assertEqual(day5.NICE, day5.judge_word_part2("qjhvhtzxzqqjkmpb"))
        self.assertEqual(day5.NICE, day5.judge_word_part2("xxyxx"))
        self.assertEqual(day5.NAUGHTY, day5.judge_word_part2("uurcxstgmygtbstg"))
        self.assertEqual(day5.NAUGHTY, day5.judge_word_part2("ieodomkazucvgmuy"))
        
