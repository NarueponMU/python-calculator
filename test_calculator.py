import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add(self):
        self.assertEqual(self.calc.add(1, 3), 4)

    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6, 2), 4)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)
    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 3), 2)

if __name__ == '__main__':
    unittest.main()