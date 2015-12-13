import unittest
import day13

EXAMPLE = ("Alice would gain 54 happiness units by sitting next to Bob.",
"Alice would lose 79 happiness units by sitting next to Carol.",
"Alice would lose 2 happiness units by sitting next to David.",
"Bob would gain 83 happiness units by sitting next to Alice.",
"Bob would lose 7 happiness units by sitting next to Carol.",
"Bob would lose 63 happiness units by sitting next to David.",
"Carol would lose 62 happiness units by sitting next to Alice.",
"Carol would gain 60 happiness units by sitting next to Bob.",
"Carol would gain 55 happiness units by sitting next to David.",
"David would gain 46 happiness units by sitting next to Alice.",
"David would lose 7 happiness units by sitting next to Bob.",
"David would gain 41 happiness units by sitting next to Carol.")

class TestDay13(unittest.TestCase):
    
    def test_mood(self):
        day13.GUESTS = ("Alice", "Bob", "Carol", "David")
        self.assertEqual(330, day13.find_best_seating(EXAMPLE))
        