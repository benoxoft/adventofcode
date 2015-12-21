import unittest
import day19

replacements = [("H" ,"HO"), ("H", "OH"), ("O", "HH"), ("e", "H"), ("e", "O")]
combs = ["HOOH", "HOHO", "OHOH", "HHHH"]
base = "HOH"

class TestDay19(unittest.TestCase):
    
    def atest_find_combinations(self):
        self.assertEqual(combs, day19.find_combinations(base, replacements))
    
    def atest_find_atoms(self):
        print day19.find_atoms_in_medecine("HOH", "H")
        print day19.find_atoms_in_medecine("HOH", "O")
    
    def atest_construct_molecule(self):
        self.assertEqual(3, day19.construct_molecule(replacements, base))
        self.assertEqual(6, day19.construct_molecule(replacements, "HOHOHO"))
        
    def test_deconstruct(self):
        self.assertEqual(3, day19.deconstruct(replacements, "e", base))
        self.assertEqual(6, day19.deconstruct(replacements, "e", "HOHOHO"))
        
if __name__ == '__main__':
    unittest.main()