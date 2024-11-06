import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(4, 7), 11)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(15, 7), 8)
        self.assertEqual(self.calc.subtract(3, 7), -4)
    
    def test_multipy(self):
        self.assertEqual(self.calc.multiply (3, 4), 12)
        self.assertEqual(self.calc.multiply(12, 9), 108)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(12, 4), 3)
        self.assertEqual(self.calc.divide(50, 10), 5)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(32, 5), 2)
        self.assertEqual(self.calc.modulo(50, 7), 1)
    

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()