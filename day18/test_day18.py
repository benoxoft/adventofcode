step0 = ("##.#.#",
         "...##.",
         "#....#",
         "..#...",
         "#.#..#",
         "####.#")

step1 = ("#.##.#",
         "####.#",
         "...##.",
         "......",
         "#...#.",
         "#.####")

step2 = ("#..#.#",
         "#....#",
         ".#.##.",
         "...##.",
         ".#..##",
         "##.###")

step3 = ("#...##",
         "####.#",
         "..##.#",
         "......",
         "##....",
         "####.#")

step4 = ("#.####",
         "#....#",
         "...#..",
         ".##...",
         "#.....",
         "#.#..#")

step5 = ("##.###",
         ".##..#",
         ".##...",
         ".##...",
         "#.#...",
         "##...#")

import unittest
import day18

class TestDay18(unittest.TestCase):
    
    def test_get_neighbors(self):
        grid = day18.parse_grid(step0)
        print day18.get_neighbor_values(grid, 0, 5)
        
    def test_decide_switch(self):
        self.assertEqual("#", day18.decide_switch(("#", "#"), "#"))
        self.assertEqual("#", day18.decide_switch(("#", "#", "#"), "#"))
        self.assertEqual(".", day18.decide_switch(("#", "#", "#", "#"), "#"))
        self.assertEqual(".", day18.decide_switch(("#", "."), "#"))
        self.assertEqual(".", day18.decide_switch(("#", ".", "."), "#"))
        self.assertEqual("#", day18.decide_switch(("#", "#", "#"), "."))
        self.assertEqual(".", day18.decide_switch(("#", "#", "#", "#"), "."))
        
    def test_grid(self):
        grid = day18.parse_grid(step0)
        grid1 = day18.parse_grid(step1)
        print grid
        print day18.change_light_grid(grid)
        print grid1
        self.assertEqual(grid1, day18.change_light_grid(grid))
        
        grid2 = day18.parse_grid(step2)
        self.assertEqual(grid2, day18.change_light_grid(grid1))
        
        grid3 = day18.parse_grid(step3)
        self.assertEqual(grid3, day18.change_light_grid(grid2))
        
        grid4 = day18.parse_grid(step4)
        self.assertEqual(grid4, day18.change_light_grid(grid3))

        grid5 = day18.parse_grid(step5)
        self.assertEqual(grid5, day18.change_light_grid(grid4))
