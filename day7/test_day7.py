import unittest
import day7

test_data = [
"123 -> x",
"456 -> y",
"x AND y -> d",
"x OR y -> e",
"x LSHIFT 2 -> f",
"y RSHIFT 2 -> g",
"NOT x -> h",
"NOT y -> i"
]

result = {
"d": 72,
"e": 507,
"f": 492,
"g": 114,
"h": 65412,
"i": 65079,
"x": 123,
"y": 456          
}

class TestDay7(unittest.TestCase):
    
    def test_solve_circuit(self):
        self.assertEqual(result, day7.solve_circuit(test_data))
        