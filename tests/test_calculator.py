# create Test Calculator class
import unittest 
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
        self.counter = self.counter + 1
        print("Setup: Creating a new Calculator instance.", self.counter)

    def tearDown(self):
        self.calc = None
        print("Teardown: Destroying the Calculator instance.")

    def test_add(self):
        result = self.calc.add(1, 2)
        self.assertEqual(result, 3)

    def test_substract(self):
        result = self.calc.substract(1, 2)
        self.assertEqual(result, -1)

    # test factorial method
    def test_factorial(self):
        result = self.calc.factorial(5)
        self.assertEqual(result, 120)
    # test factorial method with negative number   
    def test_factorial_negative(self):
        result = self.calc.factorial(-5)
        self.assertEqual(result, None)

    # TEST MULTIPLICATION METHOD
    def test_multiply(self):
        result = self.calc.multiply(2, 3)
        self.assertEqual(result, 6)

    # TEST DIVISION METHOD 
    def test_divide(self):
        result = self.calc.divide(6, 2)
        self.assertEqual(result, 3)
    # test division method with zero
    def test_divide_zero(self):
        result = self.calc.divide(6, 0)
        self.assertEqual(result, None)



        



# A class has memeber variable and method