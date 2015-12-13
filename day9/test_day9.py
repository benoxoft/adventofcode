import unittest
import day9

example = (
"London to Dublin = 464",
"London to Belfast = 518",
"Dublin to Belfast = 141"           
           )

class TestDay9(unittest.TestCase):
    
    def test_find_smallest(self):
        self.assertEqual(605, day9.find_smallest(example))
        